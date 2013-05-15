#!/usr/bin/env python
import urllib2
from bs4 import BeautifulSoup
import re

def getPriceTmall(url):
	print url
	html = urllib2.urlopen(url)
	soup = BeautifulSoup(html)
	try:
		cls = soup.find(id="J_DealRecord")
		divs = cls.div
		cons = divs.contents
		ul = cons[3]
		li = ul.li
		cons1 = li.contents
		price = cons1[1].string
	except:
		price = -1
	return 'tmall   ' + url + '    ' + price
	#return price

def getPriceTaobao(url):
	html = urllib2.urlopen(url)
	soup = BeautifulSoup(html)
	try:
		cls = soup.find(id="J_StrPrice")
		cons = cls.contents;
		price = cons[1].string
		#name = soup.title.string
	except:
		price = '-1'

	return 'taobao   ' + url + '    ' + price
	#return price

def getPrice():
	url_file = open('taobao.in', 'r')
	result_file = open('taobao.out', 'w')
	result_file.write('    page-url    ' + '    ' + 'price' + '    \n')
	for url in url_file:
		if not url:
			continue

		url = url.strip()
		if url.startswith('http://item.taobao.com/'):
			result = getPriceTaobao(url)
		elif url.startswith('http://detail.tmall.com/'):
			result = getPriceTmall(url)
		else :
			result = '------error----------'
		print result
		result_file.write(result + '\n')

	url_file.close()
	result_file.close()

if __name__ == '__main__':
	getPrice()
