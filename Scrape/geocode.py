##Return City, State from zip

import os, re, sys, urllib

def valid_HTML(urlfile):
	info = urlfile.info()
	if info.gettype() == 'text/html': 
		urltext = urlfile.read()
		return urltext
	else: 
		print 'Error retrieving geocode - HTML improperly formatted'
		sys.exit(1)

def geo(zip_geo):
	geo_data = {}
	urlfile = urllib.urlopen('http://maps.googleapis.com/maps/api/geocode/json?address='+ zip_geo + '&sensor=true')
	urltext = valid_HTML(urlfile)

	sub = re.findall(r'formatted_address" : "([\w\s\.]+), (\w\w) (\d\d\d\d\d)')
	print sub
 