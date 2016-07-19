import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('pgoapi/pgoapi')
from pgoapi import PGoApi
from utilities import f2i, h2f

from google.protobuf.internal import encoder
from geopy.geocoders import GoogleV3
from s2sphere import CellId, LatLng

import time
import re
import random
from datetime import datetime
from getpass import getpass
import argparse
import os
import platform
	
def main():
	if platform.system() == 'Windows':
		os.system("title Pokemon GO API Python")
		os.system("cls")
	else:
		# Catches "Lunux" and "Darwin" (OSX), among others
		os.system("clear")
	parser = argparse.ArgumentParser()
	parser.add_argument("-u", "--username", help="Login", required=True)
	parser.add_argument("-p", "--password", help="Password", required=True)
	parser.add_argument("-t", "--type", help="Google/PTC", required=True)
	parser.add_argument("-l", "--location", help="Location", required=True)
	args = parser.parse_args()
	print '[!] Using "%s" as login for %s..'%(args.type,args.username[:4],)
	
if __name__ == '__main__':
	main()