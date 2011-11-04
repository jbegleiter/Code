##Return Allergy Environmental Info

import os, re, sys, urllib
from geocode import geo

def route(label, d_date, z_code):
	if label == 'aw_allergies': 
		param = aw_allergy(label, z_code)
		
	elif label == 'aw_respitory': 
		param = aw_respitory(label,z_code)
	else: 
		print 'Input impropperly labeled'
		sys.exit(1)
	return param


def aw_allergy(a_date, zip):
	geo_info = geo(zip)
	city = str(geo_info[0][0]).strip().replace(' ','-').lower()
	state = str(geo_info[0][1]).strip().lower()
	url = urllib.urlopen('http://www.accuweather.com/us/'+state+'/'+city+'/'+zip+'/health-allergies.asp')

	utext = url.read()

	#Dust and Dander
	sub_start = utext.index('forecast-details.asp?fday=1\' }">')
	sub_end = utext.index('forecast-details.asp?fday=1" class')
	#should do till day = 2 to get forecast if the a_date is set to two
	utext_sub = utext[sub_start:sub_end]

	allergy_count = re.findall(r'(\d+) <span class="ac">out of',utext_sub)
	return allergy_count

def aw_respitory(r_date, zip):
	1+1


def main():
	label = sys.argv[1]
	d_date = sys.argv[2]
	zipcodes = sys.argv[3:] #[label day zip1 zip2]
	data_dict = {}
	for z_code in zipcodes:
		data_dict[z_code] = route(label,d_date,z_code)
	return data_dict

if __name__ == '__main__':
	main()