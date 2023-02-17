# conf.py

# -- Project information -----------------------------------------------------

project = 'The PD Biomarker Project'
author = 'Your Name'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {}
