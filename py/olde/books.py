#!use/local/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 2016
@author: Guoyi
'''
import urllib

def getlist():
    html = urllib.urlopen('http://www.quanshu.net/book/9/9055/').read()
    print html
getlist()
