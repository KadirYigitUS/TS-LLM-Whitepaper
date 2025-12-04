#!/usr/bin/env Rscript
suppressPackageStartupMessages({
  library(jsonlite)
  library(dplyr)
  library(purrr)
  library(readr)
  library(tidyr)
  library(httr)
  library(semscholar)
})

args <- commandArgs(trailingOnly = TRUE)
metadata_path <- ifelse(length(args) >= 1, args[[1]], "data/reference_metadata.json")
out_dir <- ifelse(length(args) >= 2, args[[2]], "data/semantic_scholar")

if (!file.exists(metadata_path)) {
  stop(sprintf("Metadata file not found: %s", metadata_path))
}

dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

`%||%` <- function(a, b) {
  if (length(a) == 0 || is.null(a) || (is.character(a) && identical(trimws(a), "")) || (length(a) == 1 && is.na(a))) {
    return(b)
  }
  a
}

first_non_na <- function(x) {
  x <- x[!is.na(x) & x != ""]
  if (length(x) == 0) {
    return(NA)
  }
  x[[1]]
}

readable_time <- function(time_val) format(time_val, "%Y-%m-%dT%H:%M:%SZ", tz = "UTC")

metadata <- read_json(metadata_path, simplifyVector = TRUE) %>%
  as_tibble()

required_cols <- c("sha_id", "file_stub", "title", "category")
missing_cols <- setdiff(required_cols, names(metadata))
if (length(missing_cols) > 0) {
  stop(sprintf("Metadata file missing required columns: %s", paste(missing_cols, collapse = ", ")))
}

force_refresh <- identical(tolower(Sys.getenv("SEMSCHOLAR_FORCE", "0")), "1")

ensure_columns <- function(df, cols) {
  for (nm in cols) {
    if (!nm %in% names(df)) {
      df[[nm]] <- NA
    }
  }
  df
}

empty_relations <- function(prefix) {
  tibble(
    !!paste0(prefix, "_paper_id") := character(),
    !!paste0(prefix, "_title") := character(),
    !!paste0(prefix, "_year") := integer(),
    !!paste0(prefix, "_doi") := character(),
    !!paste0(prefix, "_url") := character()
  )
}

standardize_relations <- function(df, prefix) {
  if (is.null(df) || length(df) == 0) {
    return(empty_relations(prefix))
  }
  df <- as_tibble(df)
  if (!"paperId" %in% names(df)) {
    return(empty_relations(prefix))
  }
  df <- ensure_columns(df, c("title", "year", "doi", "url"))
  df %>%
    transmute(
      !!paste0(prefix, "_paper_id") := paperId,
      !!paste0(prefix, "_title") := title,
      !!paste0(prefix, "_year") := suppressWarnings(as.integer(year)),
      !!paste0(prefix, "_doi") := doi,
      !!paste0(prefix, "_url") := url
    )
}

fetch_paper_semscholar <- function(paper_id) {
  tryCatch({
    res <- semscholar::s2_papers(paper_id)
    if (nrow(res) == 0) {
      NULL
    } else {
      res[1, ]
    }
  }, error = function(e) {
    warning(sprintf("semscholar::s2_papers failed for %s: %s", paper_id, e$message))
    NULL
  })
}

fetch_paper_graph <- function(paper_id) {
  fields <- paste(
    c(
      "title", "year", "url", "externalIds",
      "citations.paperId", "citations.title", "citations.year", "citations.url",
      "references.paperId", "references.title", "references.year", "references.url"
    ),
    collapse = ","
  )
  url <- sprintf("https://api.semanticscholar.org/graph/v1/paper/%s", utils::URLencode(paper_id, reserved = TRUE))
  resp <- httr::RETRY(
    "GET",
    url,
    query = list(fields = fields),
    times = 5,
    pause_base = 2,
    pause_cap = 10,
    pause_min = 1,
    terminate_on = c(400, 401, 403, 404)
  )
  status <- httr::status_code(resp)
  if (status != 200) {
    warning(sprintf("Graph API request for %s failed with status %s", paper_id, status))
    return(NULL)
  }
  payload <- httr::content(resp, as = "text", encoding = "UTF-8")
  data <- jsonlite::fromJSON(payload, simplifyDataFrame = TRUE)
  tibble(
    title = data$title %||% NA_character_,
    year = suppressWarnings(as.integer(data$year)),
    doi = data$externalIds$DOI %||% NA_character_,
    url = data$url %||% NA_character_,
    citations = list(standardize_relations(data$citations, "citations")),
    references = list(standardize_relations(data$references, "references"))
  )
}

fetch_paper <- function(paper_id) {
  result <- fetch_paper_semscholar(paper_id)
  if (!is.null(result)) {
    return(result)
  }
  message(sprintf("Falling back to Semantic Scholar Graph API for %s", paper_id))
  fetch_paper_graph(paper_id)
}

manifest_rows <- tibble()
all_nodes <- tibble()
all_edges <- tibble()

for (idx in seq_len(nrow(metadata))) {
  seed <- metadata[idx, ]
  seed_id <- seed$sha_id
  message(sprintf("Processing %s (%s)...", seed$file_stub, seed_id))
  out_file <- file.path(out_dir, paste0(seed$file_stub, "_semanticscholar_graph.json"))
  graph <- NULL
  cache_hit <- FALSE

  if (!force_refresh && file.exists(out_file)) {
    cache_hit <- TRUE
    graph <- fromJSON(out_file, simplifyVector = TRUE)
  } else {
    paper <- fetch_paper(seed_id)
    if (is.null(paper)) {
      manifest_rows <- bind_rows(
        manifest_rows,
        tibble(
          file_stub = seed$file_stub,
          sha_id = seed_id,
          output = NA_character_,
          nodes = 0L,
          edges = 0L,
          citations = 0L,
          references = 0L,
          status = "missing"
        )
      )
      next
    }

    citations_tbl <- paper$citations[[1]]
    if (is.null(citations_tbl)) {
      citations_tbl <- empty_relations("citations")
    }
    references_tbl <- paper$references[[1]]
    if (is.null(references_tbl)) {
      references_tbl <- empty_relations("references")
    }

    citations_tbl <- citations_tbl %>%
      filter(!is.na(citations_paper_id)) %>%
      mutate(type = "citation", seed_file_stub = seed$file_stub)

    references_tbl <- references_tbl %>%
      filter(!is.na(references_paper_id)) %>%
      mutate(type = "reference", seed_file_stub = seed$file_stub)

    seed_node <- tibble(
      id = seed_id,
      title = paper$title %||% seed$title,
      year = suppressWarnings(as.integer(paper$year)),
      doi = paper$doi %||% seed$doi,
      url = paper$url %||% seed$url,
      type = "seed",
      category = seed$category,
      stage = seed$stage,
      vector = seed$vector,
      seed_file_stub = seed$file_stub
    )

    citation_nodes <- citations_tbl %>%
      transmute(
        id = citations_paper_id,
        title = citations_title,
        year = suppressWarnings(as.integer(citations_year)),
        doi = citations_doi,
        url = citations_url,
        type = "citation",
        category = NA_character_,
        stage = NA_character_,
        vector = NA_character_,
        seed_file_stub = seed$file_stub
      )

    reference_nodes <- references_tbl %>%
      transmute(
        id = references_paper_id,
        title = references_title,
        year = suppressWarnings(as.integer(references_year)),
        doi = references_doi,
        url = references_url,
        type = "reference",
        category = NA_character_,
        stage = NA_character_,
        vector = NA_character_,
        seed_file_stub = seed$file_stub
      )

    nodes <- bind_rows(seed_node, citation_nodes, reference_nodes) %>%
      distinct(id, .keep_all = TRUE)

    citation_edges <- citations_tbl %>%
      transmute(
        source = citations_paper_id,
        target = seed_id,
        relation = "cited_by",
        seed_file_stub = seed$file_stub
      )

    reference_edges <- references_tbl %>%
      transmute(
        source = seed_id,
        target = references_paper_id,
        relation = "references",
        seed_file_stub = seed$file_stub
      )

    edges <- bind_rows(citation_edges, reference_edges)

    graph <- list(
      generated_at = readable_time(Sys.time()),
      seed = list(
        file_stub = seed$file_stub,
        sha_id = seed_id,
        title = seed_node$title,
        doi = seed_node$doi,
        year = seed_node$year,
        category = seed$category,
        stage = seed$stage,
        vector = seed$vector,
        url = seed_node$url
      ),
      counts = list(
        node_count = nrow(nodes),
        edge_count = nrow(edges),
        citations = nrow(citation_edges),
        references = nrow(reference_edges)
      ),
      nodes = nodes,
      edges = edges
    )

    write_json(graph, out_file, auto_unbox = TRUE, pretty = TRUE)
    message(sprintf("Saved %s", out_file))
  }

  if (is.null(graph)) {
    next
  }

  nodes <- as_tibble(graph$nodes)
  edges <- as_tibble(graph$edges)
  citation_edges <- edges %>% filter(relation == "cited_by")
  reference_edges <- edges %>% filter(relation == "references")

  manifest_rows <- bind_rows(
    manifest_rows,
    tibble(
      file_stub = seed$file_stub,
      sha_id = seed_id,
      output = out_file,
      nodes = nrow(nodes),
      edges = nrow(edges),
      citations = nrow(citation_edges),
      references = nrow(reference_edges),
      status = "ok"
    )
  )

  all_nodes <- bind_rows(all_nodes, nodes)
  all_edges <- bind_rows(all_edges, edges)

  if (!cache_hit) {
    Sys.sleep(0.5)
  }
}

if (nrow(manifest_rows) == 0) {
  stop("No Semantic Scholar graphs were generated. Check logs above.")
}

manifest_path <- file.path(out_dir, "manifest_semanticscholar.csv")
write_csv(manifest_rows, manifest_path)
write_json(manifest_rows, file.path(out_dir, "manifest_semanticscholar.json"), auto_unbox = TRUE, pretty = TRUE)

if (nrow(all_nodes) > 0) {
  combined_nodes <- all_nodes %>%
    group_by(id) %>%
    summarise(
      title = first_non_na(title),
      year = suppressWarnings(as.integer(first_non_na(year))),
      doi = first_non_na(doi),
      url = first_non_na(url),
      type = first_non_na(type),
      category = first_non_na(category),
      stage = first_non_na(stage),
      vector = first_non_na(vector),
      seeds = list(sort(unique(na.omit(seed_file_stub)))),
      .groups = "drop"
    )

  combined_edges <- all_edges %>%
    group_by(source, target, relation) %>%
    summarise(seeds = list(sort(unique(na.omit(seed_file_stub)))), .groups = "drop")

  aggregate_graph <- list(
    generated_at = readable_time(Sys.time()),
    node_count = nrow(combined_nodes),
    edge_count = nrow(combined_edges),
    manifest = manifest_rows,
    nodes = combined_nodes,
    edges = combined_edges
  )

  agg_path <- file.path(out_dir, "all_sources_semanticscholar_graph.json")
  write_json(aggregate_graph, agg_path, auto_unbox = TRUE, pretty = TRUE)
  message(sprintf("Aggregate network saved to %s", agg_path))
}

message(sprintf("Semantic Scholar harvesting complete. Manifest written to %s", manifest_path))
