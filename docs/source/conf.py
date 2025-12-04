# Configuration file for the Sphinx documentation builder.

from __future__ import annotations

import os
import sys
from datetime import datetime
from docutils import languages as docutils_languages


PROJECT_ROOT = os.path.abspath(os.path.join(__file__, "..", ".."))
sys.path.insert(0, os.path.abspath(os.path.join(PROJECT_ROOT, "..")))


# -- Project information -----------------------------------------------------

project = "TS-LLM Knowledge Stack"
author = "Kadir Yiğit US & collaborators"
copyright = f"{datetime.now():%Y}, Kadir Yiğit US"
release = "2025.12"
version = release


# -- General configuration ---------------------------------------------------

extensions = [
    "myst_parser",
    "sphinx.ext.duration",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "sphinx_autodoc_typehints",
    "sphinx_design",
]

language = "en"
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]
myst_heading_anchors = 3

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

autodoc_typehints = "description"
autodoc_mock_imports = [
    "connectedpapers",
    "markdown",
    "networkx",
    "numpy",
    "pandas",
    "plotly",
    "requests",
    "scipy",
]


# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"
html_logo = "_static/logo.png"
html_static_path = ["_static"]
html_extra_path = ["../data"]
html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 3,
    "logo_only": True,
}
html_js_files = [
    "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js",
    "js/mermaid-init.js",
    "js/tab-a11y.js",
]


# -- Internationalization ----------------------------------------------------

locale_dirs = ["../locales"]
gettext_compact = False


# -- Options for EPUB output -------------------------------------------------

epub_show_urls = "footnote"


def _ensure_tr_bibliographic_fields() -> None:
    """Docutils' Turkish locale lacks bibliographic metadata fields by default."""
    try:
        tr_lang = docutils_languages.get_language("tr")
    except Exception:
        return
    en_lang = docutils_languages.get_language("en")
    if not hasattr(tr_lang, "bibliographic_fields"):
        tr_lang.bibliographic_fields = en_lang.bibliographic_fields
    if not hasattr(tr_lang, "labels"):
        tr_lang.labels = en_lang.labels


_ensure_tr_bibliographic_fields()


def _infer_page_lang(pagename: str) -> str:
    return "tr" if pagename.startswith("tr/") else "en"


def _set_html_lang(app, pagename, templatename, context, doctree):
    context["html_lang"] = _infer_page_lang(pagename)


def setup(app):
    app.connect("html-page-context", _set_html_lang)
