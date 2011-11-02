##Return Allergy Environmental Info

import os, re, sys, urllib




def main():
	param = sys.argv[1:]
	for p in param:
		extract(p)


if __name__ == '__main__':
  main()