#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os, sys
sys.path.append(os.curdir)
from myinfo import *
# If you're getting this file without myinfo.py, feel free to 
# comment previous import and uncoment+fulfill next four lines
# AUTHOR = 'here your data'
# AUTHOR_EMAIL = 'here your data'
# SITENAME = 'here your data'
# SITEURL = 'here your data'

#ARTICLE_URL = '{slug}.html'
TIMEZONE = 'Europe/Madrid'

DEFAULT_LANG = 'ca'
NEWEST_FIRST_ARCHIVES = False # present older archives first

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

#DEFAULT_PAGINATION = 5


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# The default date you want to use. If fs, Pelican will use the file
# system timestamp information (mtime) if it can’t get date
# information from the metadata. If set to a tuple object, the default
# datetime object will instead be generated by passing the tuple to
# the datetime.datetime constructor.
DEFAULT_DATE = "fs"
DEFAULT_DATE_FORMAT = '%d/%m/%Y'

# When you don’t specify a category in your post metadata, set this
# setting to True, and organize your articles in subfolders, the
# subfolder will become the category of your post. If set to False,
# DEFAULT_CATEGORY will be used as a fallback.
USE_FOLDER_AS_CATEGORY = True
STATIC_PATHS = ["images", "resources", ]
THEME = "themes/moitheme"

# Plugings: 
PLUGIN_PATH = '//home/moi/lib/pelican-plugins/'
PLUGINS = ['navigationprevnext']

