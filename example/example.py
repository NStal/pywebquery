#!/usr/bin/python
# -*- coding: utf-8 -*-   
from pywebquery.pyWebQuery import *
p = Page("http://www.stackoverflow.com/")

#show all title match the android
for item in p.find(".question-hyperlink:title[android]").attr("title"):
    print "====================="
    print item
#show all question matched android by following the title link
for item in p.find(".question-hyperlink:title[android]").follow().find(".question.post-text").text():
    print "================================"
    print item




