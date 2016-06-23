from bs4 import BeautifulSoup, SoupStrainer
import urllib2
import csv



urlList = []

def geturlhtml(url):
	if(url[:27] == 'http://knodemy.wpengine.com'):
		if(url not in urlList):
			print url
			urlList.append(url)

			resultFile = open("output.csv",'ab')
			wr = csv.writer(resultFile, dialect='excel')
			wr.writerow([url])

			visitLink(url)

	if(url[:20] == 'knodemy.wpengine.com'):
		if(url not in urlList):
			print url
			urlList.append(url)

			resultFile = open("output.csv",'ab')
			wr = csv.writer(resultFile, dialect='excel')
			wr.writerow([url])

			visitLink('http://' + url)


def visitLink(url):
	req = urllib2.Request(url , headers={ 'User-Agent': 'Mozilla/5.0' })
	html = urllib2.urlopen(req).read()


	soup = BeautifulSoup(html)

	for a in soup.find_all('a', href=True):
	    #print "Found the URL:", a['href']
	    geturlhtml(a['href'])


visitLink('http://knodemy.wpengine.com')