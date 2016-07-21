import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('pgoapi/pgoapi')
sys.path.append('pgoapi')
from pgoapi import PGoApi
import pokecli
from utilities import f2i, h2f
import logging

from google.protobuf.internal import encoder
from geopy.geocoders import GoogleV3
from s2sphere import CellId, LatLng

import os
import platform
	
def main():
	logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(module)10s] [%(levelname)5s] %(message)s')
	logging.getLogger("requests").setLevel(logging.WARNING)
	logging.getLogger("pgoapi").setLevel(logging.INFO)
	logging.getLogger("rpc_api").setLevel(logging.INFO)
	if platform.system() == 'Windows':
		os.system("title Pokemon GO API Python")
		os.system("cls")
	else:
		# Catches "Lunux" and "Darwin" (OSX), among others
		os.system("clear")
	
	config = pokecli.init_config()
	if not config:
		return
		
	position = pokecli.get_pos_by_name(config.location)
	if config.test:
		return
		
	api = PGoApi()
	api.set_position(*position)
	if not api.login(config.auth_service, config.username, config.password):
		return
	print '[!] todo from here ..'
	exit()
	
if __name__ == '__main__':
	main()
