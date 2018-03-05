#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 10:27:23 2018

@author: lishuo
"""
from urllib.request import Request, urlopen
import json

url_template = 'https://jsonmock.hackerrank.com/api/movies/search/?Title=%s'

def  getMovieTitles(substr):
    url = url_template % substr
    req = Request(url)
    response = urlopen(req)
    the_page = response.read()
    data = json.loads(the_page)['data']
    titles = [d['Title'] for d in data]
    titles.sort()
    
    return titles
    
getMovieTitles('spiderman')