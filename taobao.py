#!/usr/bin/env python
import urllib2
from bs4 import BeautifulSoup
import chardet

def getPrice(url):
	html = urllib2.urlopen(url)
	soup = BeautifulSoup(html)
	try:
		cls = soup.find(id="deal-record")
		param = cls.p
		cons = param.contents;
		price = cons[2].string
		#name = soup.title.string
	except:
		price = '-1'

	return url + '    ' + price
	#return price

url_file = open('taobao.in', 'r')
result_file = open('taobao.out', 'w')

result_file.write('    page-url    ' + '    ' + 'price' + '    \n')

for url in url_file:
	url = url.strip()
	result = getPrice(url)
	print result
	result_file.write(result + '\n')

url_file.close();
result_file.close();
