"""Sphinx configuration."""
project = "Prometheus Wireguard Exporter (Python)"
author = "Carsten Rösnick-Neugebauer"
copyright = "2022, Carsten Rösnick-Neugebauer"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
