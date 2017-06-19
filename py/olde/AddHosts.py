#!use/local/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 20151117
@author: Guoyi
'''
import paramiko
import threading

def ssh2(ip,username,passwd,cmd):
     try:
         ssh = paramiko.SSHClient()
         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
         ssh.connect(ip,22,username,passwd,timeout=5)
         for m in cmd:
             stdin, stdout, stderr = ssh.exec_command(m)
             out = stdout.readlines()
             for o in out:
                   print o,
         print '%s\tOK\n'%(ip)
         ssh.close()
     except :
         print '%s\tError\n'%(ip)


if __name__=='__main__':
    fp=open('commands.txt','r')
arr=[]
for lines in fp:
    arr.append(lines)
print arr
cmd=arr
# cmd = ['cal','echo hello!']
username = "root"
passwd = "123"
threads = []
print "Begin......"
for i in range(1,10):
         ip = '192.168.1.'+str(i)
         a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))
         a.start()

fp.close()
