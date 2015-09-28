from bs4 import BeautifulSoup
import requests

def fetch(url):
	return requests.get(url).text

def FindUrl(sq):

	url = 'https://www.google.co.in/search?q=%s+tutorials' + sq 
	html = fetch(url)
	soup = BeautifulSoup(html)
	cites = soup.find_all('cite')
	cont = []
	for x in cites:

		cont.append(x.contents)
		urls = []
	i=0

	for x in cont:
		r = ''
		for y in x:
			r = r + str(y).replace('<b>','').replace('</b>','')
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

WF(FindUrl('python'))





