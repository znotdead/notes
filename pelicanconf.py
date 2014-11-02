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

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3
THEME = 'pelican-bootstrap3'
CUSTOM_CSS = 'static/css/main.css'
STATIC_PATHS = ['static']
SOCIAL = ()
LINKS = ()
# http://pygments.org/demo/218030/
#PYGMENTS_STYLE = 'vim'
PYGMENTS_STYLE = 'monokai'
MD_EXTENSIONS = ['nl2br']


