# -*- coding:utf-8 -*- 

import urllib,re   

def ip_jiance(t):
	return len ([i for i in t.split('.') if (0<=int(i)<=255)]) ==4


def ip_get(ip):
	url=urllib.urlopen('http://wap.ip138.com/ip_search138.asp?ip='+ ip)
	ip_html=url.read()  
	#print ip_html
	reg =re.compile(r'</b><br/><b>(.*)</b><br/>')
	f = re.findall(reg,ip_html)
	print '当前归属地是：%s'%(f[0])

def yuming_get(yuming):
	url = urllib.urlopen('http://wap.ip138.com/ip_search138.asp?ip='+yuming)
	yuming_html = url.read()
	#print yuming_html
	reg =re.compile(r'&gt;&gt;([^<]*)<br/><b>(.*)</b><br/>')
	y = re.findall(reg,yuming_html)
	#print y
	print '域名对应的IP是：%s  归属地是：%s'%(y[0][0],y[0][1])


if __name__ == '__main__':
	print "请以字符串的格式输入ip地址或者域名  如'192.163.1.1 /  wwww.baidu.com' "
	IN = input()
	if not re.findall(r'(\d{1,3}\.){3}\d{1,3}',IN):
		if re.findall(r'(\w+\.)?(\w+)(\.\D+){1,5}',IN):
			w = IN
			yuming_get(w)
		else:
			print '输入的IP或者域名格式不对'
	else:
		if ip_jiance(IN):
			x = IN
			ip_get(x)
		else:
			print u'不合法的ip'



