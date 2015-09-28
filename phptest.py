from bs4 import BeautifulSoup
import HTMLParser
import requests
import time
import operator
import random
import json
import urllib2
import urllib
import csv
import numpy as np
from lxml import html
def fetch(url):
	return requests.get(url).text
f = open('Domains','r')
dom = f.read().splitlines()
dom = set(dom)

def try_int(x):
    try:
        return int(x)
    except ValueError:
        return x

domains = []
SCts = []
LCts = []
TotalScore = []
for x in dom:
	url = "https://graph.facebook.com/fql?q=SELECT%20url,%20share_count,%20like_count%20FROM%20link_stat%20WHERE%20url=%27"+ str(x)+"%27"
	url2 = str(x)
	domains.append(url2)
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	datastr = json.dumps(data)
	datastrclean = datastr.replace('{"data": [{"url": ','').replace('}]}','')
	SCount = int(datastrclean[(datastrclean.find("share_count") + 14):(datastrclean.find("like_count") - 3)])
	LCount = int(datastrclean[(datastrclean.find("like_count") + 13):(len(datastrclean))])
	TotalScore.append(SCount + LCount)
	SCts.append(SCount)
	LCts.append(LCount)
	print url2 + str(SCount + LCount)
tp = np.array(domains)
fp = np.array(TotalScore)
combined = np.vstack((tp,fp)).T
combined = [[try_int(x) for x in lst] for lst in combined]
sLst = sorted(combined, key=lambda x: -x[1])
f = open('Ratings','w')
for x in sLst:
	for y in x:
		f.write(str(y))
		f.write("   ")
	f.write("\n")
f.close

