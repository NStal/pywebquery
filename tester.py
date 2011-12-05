#!/usr/bin/python
# -*- coding: utf-8 -*-   
from pyWebQuery import *
r = Page("http://www.verycd.com/base/movie/").find(".hot_search_keywords a").follow().find(".cname a")

#for item in r:
#    print item

for item in r.attr("href"):
    print item

