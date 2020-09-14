# -*- coding: utf-8 -*-

import sys
import os
import re

__version__ = 'latest'
if not 'READTHEDOCS' in os.environ:
    sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.abspath('custom-development/'))
sys.path.append(os.path.abspath('amazon-s3/'))
sys.path.append(os.path.abspath('extension/'))

from sphinx.locale import _
import recommonmark
from recommonmark.transform import AutoStructify

project = u'Magento 2 Extended Filesystem'
slug = re.sub(r'\W+', '-', project.lower())
version = __version__
release = __version__
author = u'George Babarus'
copyright = author
language = 'en'

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinxcontrib.httpdomain',
    'sphinx_rtd_theme',
    'recommonmark',
    'sphinx_sitemap',
    'sphinxcontrib.images'
]
html_baseurl = 'https://docs.magento.asset42.com/'
# html_baseurl = 'https://magento-file-storage-docs.babarus.ro/'
# sitemap_url_scheme = "{link}"
sitemap_filename = "sitemap-all.xml"

html_extra_path = ['robots.txt']
html_title = project + ''

images_config = {
    'override_image_directive': True
}
autosectionlabel_prefix_document = True

templates_path = ['_templates']
html_static_path = ['_static']
html_context = {
    'css_files': [
        '_static/theme_overrides.css',
        ],
     }


source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

source_parsers = {
}

exclude_patterns = [
    'requirements.txt',
    'all-pages'
]
locale_dirs = ['locale/']
gettext_compact = False

master_doc = 'index'
suppress_warnings = ['image.nonlocal_uri']
pygments_style = 'default'

intersphinx_mapping = {
    'rtd': ('https://docs.readthedocs.io/en/latest/', None),
    'sphinx': ('http://www.sphinx-doc.org/en/stable/', None),
}

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': True,
    'navigation_depth': 5
    # 'analytics_id': 'UA-54395432-3' # not working for now
}
html_theme_path = ["../.."]
html_logo = "_static/logo-wordmark-light.svg"
html_show_sourcelink = True

htmlhelp_basename = slug

latex_documents = [
    ('index', '{0}.tex'.format(slug), project, author, 'manual'),
]

man_pages = [
    ('index', slug, project, [author], 1)
]

texinfo_documents = [
    ('index', slug, project, author, slug, project, 'Miscellaneous'),
]


# Extensions to theme docs
def setup(app):
    from sphinx.domains.python import PyField
    from sphinx.util.docfields import Field

    app.add_object_type(
        'confval',
        'confval',
        objname='configuration value',
        indextemplate='pair: %s; configuration value',
        doc_field_types=[
            PyField(
                'type',
                label=_('Type'),
                has_arg=False,
                names=('type',),
                bodyrolename='class'
            ),
            Field(
                'default',
                label=_('Default'),
                has_arg=False,
                names=('default',),
            ),
        ]
    )
    app.add_config_value('recommonmark_config', {
        # 'url_resolver': lambda url: github_doc_root + url,
        'auto_toc_tree_section': 'Contents',
        'enable_math': False,
        'enable_inline_math': False,
        'enable_eval_rst': True,
    }, True)
    app.add_transform(AutoStructify)
