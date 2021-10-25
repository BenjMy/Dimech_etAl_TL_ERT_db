# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

# -- Project information -----------------------------------------------------

project = 'DimechetAl_TLERTdb'
copyright = '2021, B. Mary, A. Dimech'
author = 'B. Mary, A. Dimech'
# The short X.Y version
version = '0.1.1'
# The full version, including alpha/beta/rc tags
release = '0.1.1'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'



# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'nbsphinx', # to include jupyter notebook as sphinx doc page
    'sphinx.ext.mathjax',
    'sphinx.ext.autosectionlabel'
]

nbsphinx_execute = 'always'
nbsphinx_kernel_name = 'Dimech-env'

# Produce pages for each class and function
autosummary_generate = True
autodoc_default_flags = ['members', 'inherited-members']


# Configure the inline plots from matplotlib plot_directive
plot_formats = [("png", 90)]
plot_html_show_formats = False
plot_html_show_source_link = False

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']
# source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_logo = 'img/logo.png'
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

# import guzzle_sphinx_theme

# html_favicon = 'img/logo.png'
# html_title = project + ' version ' + release
# html_theme_path = guzzle_sphinx_theme.html_theme_path()
# html_theme = 'guzzle_sphinx_theme'

# html_theme_options = {
#     'navigation_with_keys': True,
#     'project_nav_name': project,
#     'base_url': 'https://nbsphinx.readthedocs.io/en/guzzle-theme/',
#     'globaltoc_depth': 3,
#     #'globaltoc_collapse': False,
# }
# html_sidebars = {
#     '**': ['logo-text.html', 'globaltoc.html', 'searchbox.html']
# }

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'ERTdb'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'ERTdb.tex', 'ERTdb Documentation',
     'B. Mary, A. Dimech', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'ERTdb', 'ERTdb Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'ERTdb', 'ERTdb Documentation',
     author, 'ERTdb', 'ERTdb is a Python wrapper for CATHY allowing mesh creation, forward and inverse modeling, and simple output visualization of CATHY simulations',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']
