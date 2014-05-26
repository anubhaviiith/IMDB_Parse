#Anubhav Srivastava
#@IIIT-Hyderabad
#IMDB Ratings Finder

import re
from bs4 import BeautifulSoup
import urllib2
import os
import sys
import time

start_time = time.time()

final=[]
fileList = []
ans=[]
rootdir = '/media/Seagate Backup Plus Drive/Movies'
for root, subFolders, files in os.walk(rootdir):
	for file in files:
		l=[]
		if '.avi' in file:
			l=file.split('.avi')
		if '.mkv' in file:
			l=file.split('.mkv')
		if '.mp4' in file:
			l=file.split('.mp4')
		try:	
			ans.append(l[0])
		except:
			continue
for query in ans:
	newquery=''
	querynb=query.split()
	if(len(querynb)==1):
		querynb=query.split('.')
	for u in range(0,len(querynb)):
		newquery+=querynb[u]+'+'
	newquery=newquery[:-1]
	try :
		response=urllib2.urlopen('http://www.imdb.com/find?q='+newquery+'&s=all')
		soup=BeautifulSoup(response.read())
	
		for link in soup.find_all('a'):
			a=(link.get('href'))
			if a!=None and 'title/' in a:
				link='http://www.imdb.com'+ a
				break
		response=urllib2.urlopen(link)
		soup=BeautifulSoup(response.read())
		for link in soup.find_all('div',{'class':'titlePageSprite star-box-giga-star'}):
			zam=query + '              :            ' + link.string 
			final.append(zam)
	except:
		zam=query + '              :            ' + 'ERROR(404)'
		final.append(zam)
for i in final:
	print i

print time.time() - start_time, "seconds"
