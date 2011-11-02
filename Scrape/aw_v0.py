##Return Allergy Environmental Info

import os, re, sys, urllib
from geocode import *

def route(param):
	if param[0] == 'aw_allergies': 
		for zip in param[2:]: #param[1] is date
			aw_allergy(param[1],zip)

	elif param[0] == 'aw_respitory': 
		for zip in param[2:]:
			aw_respitory(param[1],zip)


def aw_allergy(a_date, zip):
	geo_info = geo(zip)
	#url = urllib.open('http://www.accuweather.com/us/pa/philadelphia/19019/health-allergies.asp')

def aw_respitory(r_date, zip):


def main():
	params = sys.argv[1:] #[label day zip1 zip2]
	for param in params:
		route(param)

if __name__ == '__main__':
  main()