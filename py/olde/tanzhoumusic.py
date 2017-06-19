#!use/local/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 2016
@author: Guoyi
http://s.music.163.com/search/get/?type=1&s=love&limit=9
出现ASCLL基本都是编码问题
遇到json[]list就是我们所要的内容
'''

from Tkinter import *
import tkMessageBox
import urllib
import json
import time
import ctypes
def music():
    e1 = entry.get()
    # if not e1.strip():tkMessageBox.showinfo('提示','请先输入歌曲信息！')
    if not e1.strip():  #not取反  if not 假的取反
    #
    # # if e1.strip()=='':
    # # if entry.get() == '':
        tkMessageBox.showinfo('提示','请先输入歌曲信息！')
        return
    else:
        listbox.delete(0,listbox.size())
        musicname =urllib.quote(e1.encode('utf-8'))
        # html = urllib.urlopen('http://s.music.163.com/search/get/?type=1&s=love&limit=9').read()
        html = urllib.urlopen('http://s.music.163.com/search/get/?type=1&s=' + musicname + '&limit=10').read()
        js = json.loads(html)
        suoyi = 0
        for i in js['result']['songs']:
            # print i
            listbox.insert(suoyi,i['name']+'('+i['artists'][0]['name']+')')
            print i['name']

        # print js['result']['songs']
        # print html

root = Tk()
root.title('音乐播放器')
# root.geometry('500x309+800+200')
root.geometry('+800+200')
entry = Entry(root)
entry.pack()
# Entry(root).pack()
Button(root, text='搜索歌曲', command=music).pack()
# Button(root, text='播放歌曲', command=music).pack()
var = StringVar()
listbox = Listbox(root, width=50, listvariable=var)
listbox.pack()
root.mainloop()
