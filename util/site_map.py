#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019-04-14 12:40
# @Author: yanmiexingkong
# @email : yanmiexingkong@gmail.com
# @File  : site_map.py
from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)


sitemaps = {
    'static': StaticViewSitemap,
}
