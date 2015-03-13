#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'znotdead'
SITENAME = u'Notes'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
SOCIAL = ()

USE_FOLDER_AS_CATEGORY = True

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# https://github.com/znotdead/pelican-themes/tree/master/pelican-bootstrap3
THEME = '../pelican-bootstrap3/'
CUSTOM_CSS = 'static/css/main.css'
CUSTOM_JS = [
    '/static/js/jquery-latest.js',
    '/static/js/jquery.tablesorter.min.js',
    '/static/js/main.js',
]
STATIC_PATHS = ['static']
LINKS = ()

FAVICON = 'static/img/ico/logo.png'
SITELOGO = 'static/img/ico/logo.png'
SITELOGO_SIZE = 50
TOUCHICON = 'static/img/ico/logo.png'
CATEGORIES_LOGO = True
# http://pygments.org/demo/218030/
#PYGMENTS_STYLE = 'vim'
PYGMENTS_STYLE = 'monokai'
MD_EXTENSIONS = ['nl2br', 'tables', 'fenced_code', 'codehilite(css_class=highlight)',]

DISPLAY_CATEGORIES_ARTICLES_AS_LIST = ('songs', 'car', 'knitting', 'modeling', 'programming',
                                       'recipes', 'vim',)

# Plugins
#from pelican_tag_cloud_by_category import tag_cloud_by_category
PLUGIN_PATHS = ['../pelican_tag_cloud_by_category/',]
PLUGINS = ['tag_cloud_by_category', ]

DISPLAY_TAGS_FOR_CATEGORY = True
DISPLAY_TAGS_INLINE = True

#DISQUS_SITENAME = 'znotdeadnotes'
#GOOGLE_ANALYTICS = 'UA-57013075-1'
