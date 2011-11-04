##Return City, State from zip

import re, urllib



def geo(zip_geo):
	geo_data = {}
	urlfile = urllib.urlopen('http://maps.googleapis.com/maps/api/geocode/json?address='+ zip_geo + '&sensor=true')
	urltext = urlfile.read()

	sub = re.findall(r'formatted_address" : "([\w\s\.]+), (\w\w) (\d\d\d\d\d)',urltext)
	#print sub
	return sub[:1]
 

# def valid_HTML(urlfile):
# 	info = urlfile.info()
# 	if info.gettype() == 'text/html': 
# 		urltext = urlfile.read()
# 		return urltext
# 	else: 
# 		print 'Error retrieving geocode - HTML improperly formatted'
# 		sys.exit(1)