#!/usr/bin/env Rscript
suppressPackageStartupMessages({
  library(jsonlite)
  library(dplyr)
  library(visNetwork)
  library(htmlwidgets)
  library(scales)
})

args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 2) {
  stop("Usage: network_widgets.R <graph_json> <output_html>")
}

graph_path <- args[[1]]
out_path <- args[[2]]

graph_data <- fromJSON(graph_path)
if (!"nodes" %in% names(graph_data)) {
  stop("Graph JSON missing 'nodes' array.")
}

edge_field <- if ("links" %in% names(graph_data)) {
  "links"
} else if ("edges" %in% names(graph_data)) {
  "edges"
} else {
  stop("Graph JSON missing 'links' or 'edges' array.")
}

nodes <- as_tibble(graph_data$nodes)
if (!"citations" %in% names(nodes)) {
  nodes$citations <- NA_real_
}
nodes <- nodes %>%
  mutate(
    citations = ifelse(is.na(citations) | citations <= 0, 1, citations),
    size = scales::rescale(citations, to = c(10, 40)),
    color = case_when(
      tolower(category) %in% c("primary", "primary sources", "primary sources (the seminal llm papers)") ~ "#264653",
      tolower(category) %in% c("secondary", "secondary sources", "secondary sources (nlp & engineering foundations)") ~ "#2a9d8f",
      tolower(category) %in% c("tertiary", "tertiary sources", "tertiary sources (translation theory & critique)") ~ "#e9c46a",
      TRUE ~ "#f4a261"
    ),
    hover = ifelse(is.na(doi) | doi == "", title, paste(title, "\n", doi))
  ) %>%
  transmute(id = id, label = title, size = size, color = color, title = hover)

edges_raw <- as_tibble(graph_data[[edge_field]])
if (!"source" %in% names(edges_raw)) {
  edges_raw$source <- NA
}
if (!"from" %in% names(edges_raw)) {
  edges_raw$from <- NA
}
if (!"target" %in% names(edges_raw)) {
  edges_raw$target <- NA
}
if (!"to" %in% names(edges_raw)) {
  edges_raw$to <- NA
}
if (!"weight" %in% names(edges_raw)) {
  edges_raw$weight <- NA_real_
}
if (all(is.na(edges_raw$source)) && all(is.na(edges_raw$from))) {
  stop("Edges must contain 'source' (or 'from') and 'target' columns.")
}
if (all(is.na(edges_raw$target)) && all(is.na(edges_raw$to))) {
  stop("Edges must contain 'target' (or 'to') column.")
}

edges <- edges_raw %>%
  transmute(
    from = coalesce(source, from),
    to = coalesce(target, to),
    value = ifelse(is.na(weight), 1, weight)
  )

widget <- visNetwork(nodes, edges, width = "100%", height = "600px") %>%
  visPhysics(stabilization = TRUE) %>%
  visLegend() %>%
  visOptions(highlightNearest = TRUE, nodesIdSelection = TRUE)

saveWidget(widget, file = out_path, selfcontained = TRUE)
cat(sprintf("Widget saved to %s\n", out_path))
