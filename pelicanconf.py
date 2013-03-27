#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Dan'
SITENAME = u"Dan DeSousa's Blog"
SITEURL = ''

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = u'en'

# Blogroll
LINKS =  tuple([
  #('Jinja2', 'http://jinja.pocoo.org'),
  ])

# Social widget
SOCIAL = (
    ('Twitter', 'http://twitter.com/dandesousa'),
    ('Github', 'http://github.com/dandesousa'),
    ('Google Plus', 'https://plus.google.com/114589102912613956952'),
    ('Facebook', 'https://facebook.com/daniel.sousa'),
    )

DEFAULT_PAGINATION = 10

PLUGINS = ['pelican.plugins.assets',]
STATIC_PATHS = ['images', 'wp-content']
FILES_TO_COPY = (('CNAME', 'CNAME'),)

USE_FOLDERS_AS_CATEGORY=False
DISPLAY_PAGES_ON_MENU=True

# Social network
DISQUS_SITENAME = "dandesousacom"
TWITTER_USERNAME = "dandesousa"

# Tracking
GOOGLE_ANALYTICS = "UA-10113677-1"

# Search
GOOGLE_SITE_SEARCH_URL = "http://dandesousa.com"
