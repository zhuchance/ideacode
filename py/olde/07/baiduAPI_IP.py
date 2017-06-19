#!use/local/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 2016
@author: Guoyi
'''

import sys, urllib, urllib2, json

ipadd = raw_input("请输入IP地址")

url = 'http://apis.baidu.com/apistore/iplookupservice/iplookup?ip=' + ipadd
# url = 'http://apis.baidu.com/apistore/iplookupservice/iplookup?ip=183.206.27.253'
#
print url

req = urllib2.Request(url)

req.add_header("apikey", "自己的apikey")


resp = urllib2.urlopen(req)
content = resp.read().decode('unicode_escape')
print content
