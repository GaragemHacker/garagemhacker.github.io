#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

import xmltodict
from html2text import html2text

xml = open('garagemhacker.wordpress.2016-02-02.xml').read()
parsed = xmltodict.parse(xml)

items = parsed['rss']['channel']['item']

filter_by = lambda items, type_: items['wp:post_type'] == type_

attachments = filter(lambda items: items['wp:post_type'] == 'attachment', items)
posts = filter(lambda items: items['wp:post_type'] == 'post', items)
pages = filter(lambda items: items['wp:post_type'] == 'page', items)

total_posts = len(posts)
total_attachments = len(attachments)
total_pages = len(pages)

for i in posts:
    try:
        date = datetime.datetime.strptime(i['pubDate'],
                                          '%a, %d %b %Y %H:%M:%S +0000')
    except ValueError:
        print 'Malformed date {}'.format(i['pubDate'])

    categories = []
    try:
        cats = i['category']
        # list of categories
        if type(cats) == list:
            for cat in cats:
                categories.append(cat[2]['#text'])
        else:
            # single category
            categories.append(cats['#text'])
    except KeyError:
        pass

    if len(categories):
        categories = filter(lambda x: x != 'Uncategorized', categories)
        categories = ','.join(categories)
    else:
        categories = ''

    slug = filter(None, i['link'].split('/'))[-1]

    try:
        content = html2text(i['content:encoded'])
    except:
        content = ''

    print u"""
Title: {}
Date: {}
Category: {}
Slug: {}
Authors: Garagem

{}
""".format(i['title'], date, categories, slug, content)
