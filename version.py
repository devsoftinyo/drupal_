import urllib2,re
def get_version(url):
	contents = urllib2.urlopen(url).read()
	splitted = contents.split()
	return splitted[1]