"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import sys
# import os
# sys.path.insert(0, os.path.abspath('.'))
import os
from egdocs.xml_docs import build
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:
	import sphinx_rtd_theme
	from time import sleep
	html_theme = 'sphinx_rtd_theme'
	html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
	# Sleep to allow time to clear _build, since PyCharm doesn't support sequential configurations
	sleep(10)

# -- Project information -----------------------------------------------------

project = 'eaw-godot-docs'
# noinspection PyShadowingBuiltins
copyright = '2020, luke13139'
author = 'luke13139'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	'sphinx.ext.intersphinx',
	'sphinx.ext.graphviz',
	'sphinx.ext.mathjax',
	'sphinx.ext.todo',
]

# sphinx.ext.intersphinx Configuration
# Link Latest Godot Docs
intersphinx_mapping = {
	'godot': ('https://docs.godotengine.org/en/latest/', None)
}

# sphinx.ext.todo Configuration
# Include TODOs in final output, should be disabled on documentation release
todo_include_todos = True

# Set default role to ref
default_role = 'ref'

# Try settings the homepage URL to readme
# html_baseurl = ""

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to include when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
include_patterns = ["/basegame", "/port", "index.rst"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

# Sphinx RTD Theme Options
html_theme_options = {
	# 'canonical_url': '',
	# 'analytics_id': 'UA-XXXXXXX-1',
	# 'logo_only': False,
	'display_version': True,
	'prev_next_buttons_location': 'bottom',
	'style_external_links': True,
	# 'vcs_pageview_mode': '',
	# 'style_nav_header_background': 'white',
	# Toc options
	'collapse_navigation': False,
	'sticky_navigation': True,
	'navigation_depth': 4,
	'includehidden': True,
	'titles_only': True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Run build
build()
