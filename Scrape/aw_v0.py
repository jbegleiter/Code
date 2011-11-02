##Return Allergy Environmental Info

import os, re, sys, urllib
from geocode import *

def route(label, d_date, z_code):
	if label == 'aw_allergies': 
		aw_allergy(label, z_code)

	elif label == 'aw_respitory': 
		aw_respitory(label,z_code)
	else: 
		print 'wrong'
		sys.exit(1)


def aw_allergy(a_date, zip):
	geo_info = geo(zip)
	print geo_info
	#url = urllib.open('http://www.accuweather.com/us/pa/philadelphia/19019/health-allergies.asp')

def aw_respitory(r_date, zip):
	1+1


def main():
	label = sys.argv[1]
	d_date = sys.argv[2]
	zipcodes = sys.argv[3:] #[label day zip1 zip2]
	for z_code in zipcodes:
		route(label,d_date,z_code)

if __name__ == '__main__':
  main()