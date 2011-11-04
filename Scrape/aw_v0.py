##Return Allergy Environmental Info

import os, re, sys, urllib
from geocode import geo

def route(label, d_date, z_code):
	if label == 'aw_allergies': 
		param = aw_allergy(label, z_code)
		
	elif label == 'aw_respitory': 
		param = aw_respitory(label,z_code)
	else: 
		print 'wrong'
		sys.exit(1)
	return param


def aw_allergy(a_date, zip):
	geo_info = geo(zip)
	print geo_info
	city = geo_info[0].strip().replace(' ','-').lower()
	state = geo_info[1].strip().lower()
	url = urllib.open('http://www.accuweather.com/us/'+state+'/'+city+'/'+zip+'/health-allergies.asp')

	utext = url.read()

	sub_start = utext.index('href: \'http://www.accuweather.com/us/'+state+'/'+city+'/'+zip'+/forecast-details.asp?fday=1')
	sub_end = utext.index('href="http://www.accuweather.com/us/'+state+'/'+city+'/'+zip'+/forecast-details.asp?fday=1')
	#should do till day = 2 to get forecast if the a_date is set to two
	utext_sub = utext[sub_start:sub_end]

	#Get Allergy info
	allergy_count = re.find(r'(\d+) <span class="ac">out of')
	return allergy_count

def aw_respitory(r_date, zip):
	1+1


def main():
	label = sys.argv[1]
	d_date = sys.argv[2]
	zipcodes = sys.argv[3:] #[label day zip1 zip2]
	data_dict = {}
	for z_code in zipcodes:
		data_dict(z_code) = route(label,d_date,z_code)
	return data_dict

if __name__ == '__main__':
	main()