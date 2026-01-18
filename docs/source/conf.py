import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Read the docs'
author = 'Oscar Witman'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']
