import importlib.util
assert importlib.util.find_spec("sphinx_design"), "sphinx_design not installed in RTD build"


# Configuration file for the Sphinx documentation builder.

def setup(app):
    app.add_css_file("custom.css")

# -- Project information

project = 'Agri-scHub'
copyright = '2025, SongLiLab'
author = 'SongLiLab'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    "myst_parser",
    "sphinx_needs",
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_design',
]

myst_enable_extensions = [
    "colon_fence",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_theme_options = {
    # Sidebar behavior
    "collapse_navigation": True,   # collapse siblings by default
    "sticky_navigation": True,     # keep sidebar visible on scroll
    "navigation_depth": 3,         # how many levels to show in the nav
    "titles_only": False,          # show page titles + sections
    # Branding (optional)
    "logo_only": False,
    "display_version": False,
}

html_static_path = ['_static']
html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css",
    "custom.css"
]

needs_types = [
    dict(directive="publication", title="Publication", prefix="PUB", color="#BFD8D2", style="node"),
]

needs_default_layout = "clean"

