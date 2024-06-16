import oldv

project = oldv.__name__
author = "osoken"

version = oldv.__version__
release = oldv.__version__

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
exclude_patterns = ["main.py"]

language = "en"
