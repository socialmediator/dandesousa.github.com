#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Dan'
SITENAME = u"Dan DeSousa's Blog"
SITEURL = ''
COPYRIGHT_HOLDER = u'Dan DeSousa'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = u'en'

# Blogroll
LINKS =  tuple([
  #('Jinja2', 'http://jinja.pocoo.org'),
  ])

# Social widget (timberland and others)
SOCIAL = (
    ('Twitter', 'http://twitter.com/dandesousa'),
    ('Github', 'http://github.com/dandesousa'),
    ('Google Plus', 'https://plus.google.com/114589102912613956952'),
    ('Facebook', 'https://facebook.com/daniel.sousa'),
    )

DEFAULT_PAGINATION = 3

PLUGINS = ['pelican.plugins.assets',]
STATIC_PATHS = ['images', 'wp-content']
FILES_TO_COPY = (('CNAME', 'CNAME'),)

USE_FOLDERS_AS_CATEGORY=False
DISPLAY_PAGES_ON_MENU=True


DATE_FORMATS = {
 'en':"%A, %B %d %Y %I:%M %p",
 }

MENUITEMS = [
    ('About', '/pages/about')
]


ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Social network
DISQUS_SITENAME = "dandesousacom"
TWITTER_USERNAME = "dandesousa"

# Tracking
GOOGLE_ANALYTICS = "UA-10113677-1"

# Search
GOOGLE_SITE_SEARCH_URL = "http://dandesousa.com"

# Showcase 
TWITTER_URL = 'http://twitter.com/dandesousa'
FACEBOOK_URL = 'https://facebook.com/daniel.sousa'
GITHUB_URL = 'https://github.com/dandesousa'
