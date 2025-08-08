```R
Log <- function(texto) {
  linea <- paste0(format(Sys.time(), "%Y-%m-%d %H:%M:%S"), " | ", texto)
  writeLines(linea, "workflow_log.txt", append = TRUE)
}

Log("Inicio del preprocesamiento")

```
