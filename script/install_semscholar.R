#!/usr/bin/env Rscript
repos <- "https://cloud.r-project.org"
if (!requireNamespace("remotes", quietly = TRUE)) {
  install.packages("remotes", repos = repos)
}
if (!requireNamespace("semscholar", quietly = TRUE)) {
  remotes::install_github("njahn82/semscholar", upgrade = "never")
} else {
  message("semscholar is already installed; skipping remotes::install_github().")
}
