from bs4 import BeautifulSoup
import requests
import time
import json
import random
def fetch(url):
	headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0',
				'Connection':'keep-alive',
				'Cookie':'',
				'Cache-Control':'max-age=0',
				'Accept-Language':'en-US,en;q=0.5'
	}
	return requests.get(url).text

	time.sleep(random.randint(10,20))

def FindUrl(sq,pg):

	url = 'https://www.google.co.in/search?q='+ sq +'+tutorials&start=' + str((pg-1)*10)
	print url
	html = fetch(url)
	soup = BeautifulSoup(html)
	cites = soup.find_all('cite')

	
	cont=[]
	for x in cites:
		cont.append(x.contents)
	
	urls=[]
	for x in cont:
		r = ''
		for y in x:
			r = r + str(y).replace('<b>','').replace('</b>','').replace('>','/')
		urls.append(r)

	results=[]
	for i in urls:
		r = str(i)
		if(r.find('www')==0):
			r = 'http://' +r
		if(r.find('www')==-1 & r.find('https:')==-1):
			r = 'http://' +r
		results.append(r)
	return results
def WF(array =[]):
	f = open('DataUrls', 'a+')
	for x in array:
		f.write(str(x)+'\n')
	f.close
	
def cleanup(array=[]):
	f = open('Domains' , 'a+')
	for x in array:
		r = str(x)
		ind = r.find('/', 9 ,len(r))
		r2 = r[0:ind]
		r2 =str(r2).replace('http://','').replace('https://', '').replace('www.','')
		f.write(str(r2)+'\n')
	f.close
	





