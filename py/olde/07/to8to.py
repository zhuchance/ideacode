#!use/local/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 2016
@author: Guoyi
User-Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36
权限管理机制：cookies

sid:3925694
uid:6383185
did:670462

'''

import urllib2
import cookielib
import re

c = cookielib.LWPCookieJar()
#创建一个可以保存cookies的对象
cookie = urllib2.HTTPCookieProcessor(c)
opener = urllib2.build_opener(cookie)


def login(user, passwd):
    url = 'http://www.to8to.com/new_login.php'
    data = 'ismd5=0&referer=http%3A%2F%2Fsz.to8to.com%2F&val=' + user + '&password=' + passwd
    # data = ''+user+''+passwd
    req = urllib2.Request(url, data=data)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')
    # html = urllib2.urlopen(req).read()
    html = opener.open(req).read()
    print html
    if user in html:
        return True
    return False
def getid(url):
    html = opener.open(url).read()
    reg = r"var gdid = '(.*?)'"
    sid = re.findall(reg,html)[0]
    reg = r'var owner_id = "(.*?)"'
    uid = re.findall(reg,html)
    reg = r'var idr = "(.*?)"'
    did = re.findall(reg,html)
    print sid, uid, did


# getid("http://www.to8to.com/riji/" + )

def getlist():
    html = opener.open('http://www.to8to.com/riji/cd').read()
    print html
    reg = r'class="diary_author" href="(.*?)" '

# login('zhuchance','0381160344')
if login('zhuchance','0381160344'):
    print "登陆成功~~"
else:
    print "登陆失败！"
