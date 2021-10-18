# Configuration file for the Sphinx documentation builder.
import sys
import os
import plotly
# -- Project information
    
sys.path.insert(0, os.path.abspath('../'))

project = 'ertdb'
copyright = '2021, B. Mary, A. Dimech'
author = 'B. Mary, A. Dimech'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'jupyter_sphinx.execute',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
]


intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

exclude_patterns = ['_build', '**.ipynb_checkpoints']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
