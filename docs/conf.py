#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# wurst documentation build configuration file, created by
# sphinx-quickstart on Wed Jun 21 13:30:42 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.

import sys
from unittest.mock import MagicMock
from os.path import abspath, dirname

class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
            return MagicMock()


MOCK_MODULES = [
  "bw2data",
  "bw2data.backends.peewee",
  "bw2data.database",
  "appdirs",
  "bw2io.importers.base_lci",
  "country_converter",
  "numpy",
  "pythonjsonlogger",
  "tqdm",
  # "fiona.crs",
  # "numpy",
  # "pyproj",
  # "rtree",
  # "rasterio",
  # "rasterio.rio.helpers",
  # "rasterio.crs",
  # "rasterio.features",
  # "rasterio.warp",
  # "rasterstats",
  # "rasterstats.io",
  # "rasterstats.utils",
  # "shapely",
  # "shapely.geometry",
  # "shapely.geos",
  # "shapely.ops",
]
sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.1.dev'
# The full version, including alpha/beta/rc tags.
release = '0.1.dev'

# Make sure we use this copy of Wurst
sys.path.insert(1, abspath(dirname(dirname(__file__))))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.mathjax']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'wurst'
copyright = '2017, Chris Mutel'
author = 'Chris Mutel'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'wurstdoc'


# -- Options for LaTeX output ---------------------------------------------

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
    (master_doc, 'wurst.tex', 'wurst Documentation',
     'Chris Mutel', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'wurst', 'wurst Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'wurst', 'wurst Documentation',
     author, 'wurst', 'One line description of project.',
     'Miscellaneous'),
]



