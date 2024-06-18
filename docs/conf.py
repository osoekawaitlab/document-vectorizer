import oldv

project = oldv.__name__
author = "osoken"

version = oldv.__version__
release = oldv.__version__

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinxcontrib.autodoc_pydantic",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

language = "en"

autodoc_pydantic_model_show_json = True
autodoc_pydantic_model_show_config_summary = False
