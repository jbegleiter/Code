##Return Allergy Environmental Info
# Input :

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
	allergy_count = {}
	geo_info = geo(zip)
	city = str(geo_info[0][0]).strip().replace(' ','-').lower()
	state = str(geo_info[0][1]).strip().lower()
	url = urllib.urlopen('http://www.accuweather.com/us/'+state+'/'+city+'/'+zip+'/health-allergies.asp')

	utext = url.read()

	#Dust and Dander
	sub_start_dd = utext.index('forecast-details.asp?fday=1\' }">')
	sub_end_dd = utext.index('forecast-details.asp?fday=1" class')
	#should do till day = 2 to get forecast if the a_date is set to two
	utext_sub_dd = utext[sub_start_dd:sub_end_dd]

	dd_value = re.findall(r'(\d+) <span class="ac">out of',utext_sub_dd)
	allergy_count['dust_dander'] = float(dd_value[0])
	
	#Grass Pollen
	sub_start_gp = utext.index('<h4 class="lt">Grass Pollen</h4>')
	sub_end_gp = utext.index('#pollen-index-2\', strut: \'.comment')
	utext_sub_gp = utext[sub_start_gp:sub_end_gp]
	gp_value = re.findall(r'Rating: </span>([\d\s\.]+)<span class="ac">out of 10',utext_sub_gp)
	allergy_count['grass_pollen'] = float(str(gp_value[0]).strip())

	#Ragweed Pollen
	sub_start_rp = utext.index('<h4 class="lt">Ragweed Pollen</h4>')
	sub_end_rp = utext.index('id="pollen-index-3" class="panel-sml health"')
	utext_sub_rp = utext[sub_start_rp:sub_end_rp]
	rp_value = re.findall(r'Rating: </span>([\d\s\.]+)<span class="ac">out of 10',utext_sub_rp)
	allergy_count['ragweed_pollen'] = float(str(rp_value[0]).strip())

	#Tree Pollen
	sub_start_tp = utext.index('<h4 class="lt">Tree Pollen</h4>')
	sub_end_tp = utext.index('id="pollen-index-2" class="panel-sml health"')
	utext_sub_tp = utext[sub_start_tp:sub_end_tp]
	#print utext_sub_tp
	tp_value = re.findall(r'Rating: </span>([\d\s\.]+)<span class="ac">out of 10',utext_sub_tp)
	allergy_count['tree_pollen'] = float(str(tp_value[0]).strip())

	
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
	print data_dict
	return data_dict

if __name__ == '__main__':
	main()