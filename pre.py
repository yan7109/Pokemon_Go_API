import base64
import time
import re
import config
import login
import random
from random import randint
try:
	import pokemon_pb2
	import pokemon
except:
	pass
try:
	from cStringIO import StringIO
except ImportError:
	from StringIO import StringIO

def generate_random_long():
	return long(random.choice(range(0,10000000)))
	
def get_api(access_token,first_data):
	try:				
		#r=config.s.post(config.api_url,data=base64.b64decode(pokemon.generate_login(access_token)),verify=False)
		r=config.s.post(config.api_url,data=first_data,verify=False)
		pok = pokemon_pb2.Login()
		pok.ParseFromString(r.content)
		return 'https://'+pok.api_point+'/rpc'
	except:
		print '[-] server offline'
		time.sleep(3)
		get_api(access_token)
		
def use_api(target_api,prot1):
	if config.debug:
		print '[!] using api:',target_api
	r=config.s.post(target_api,data=prot1,verify=False)
	return r.content

def gen_first_data(access_token):
	login_request = pokemon_pb2.login_request()
	login_request.time = 2
	login_request.unknown12 = 72185515343875
	login_request.rpc_id = 72185515343874
	login_request.auth.provider = 'google'
	login_request.auth.token.contents = access_token
	
	req1 = login_request.requests.add()
	req1.type = 2
	req2 = login_request.requests.add()
	req2.type = 126
	req3 = login_request.requests.add()
	req3.type = 4
	req4 = login_request.requests.add()
	req4.type = 129
	req5 = login_request.requests.add()
	req5.type = 5
	return login_request.SerializeToString()
	
found_stops=[
('90ba85b5ce97413eb95ecda5b52e74e4.16',0x404aca4b9884c6a4,0x4023e5f30e7ff584),
('b79b4abdf8304effba43f617e8bade8d.16',0x404aca3ca7503b82,0x4023e58c6d612c6b),
('03cb3d6dd7824b68a5f7db4c365137fa.16',0x404aca367e414e7f,0x4023e5cdd50a88f0),
('6c9dba38db914aba98a49d8717b56210.16',0x404aca24463065f9,0x4023e5432873bc90),
('a7a31bc8faeb485ca5431cd45c172650.16',0x404aca236c15d2d0,0x4023e5ef8487b99d),
('367464892aa146c2bfccd7574a8e8769.16',0x404aca4ee7c49fd8,0x4023e528ae74f2f1),
('09ef4f1508a8412f92b3e748c1643eba.16',0x404aca5b0ff10ecb,0x4023e630014f8b59),
('353011ca6ea0457a81be71b9f85f354b.16',0x404aca67620ee8d1,0x4023e610cf5b1c86),
('f9b455db6b75493eb95b28d30d6ef18e.16',0x404aca69ad42c3ca,0x4023e5a3e39f7729),
('3d1249956c6d49e1b4e99382c8d21a31.16',0x404aca6601bc98a2,0x4023e508b32ce896),
]
	
def gen_stop_data(ses,cur_session):
	stop_request = pokemon_pb2.stop_request()
	stop_request.time = 2 #1
	#stop_request.rpc_id = 9077956684869009422 #3 static
	stop_request.rpc_id = 2212820743501119519 #3 static
	stop_request.unk1 = cur_session[1]-randint(0,9) #7
	stop_request.unk2 = cur_session[2]-randint(0,9) #8
	stop_request.unk3 = 0x4050400000000000 #9 static
	stop_request.unknown12 = 23229 #12 static
	stop_request.sess.ses1 = ses.ses1 #12
	stop_request.sess.time = ses.time #12
	stop_request.sess.ses2 = ses.ses2 #12
	
	req1 = stop_request.requests.add()
	req1.type = 101
	req1.message.unknown4 = cur_session[0]
	req1.message.unknown5 = cur_session[1]-randint(0,9)
	req1.message.unknown6 = cur_session[2]-randint(0,9)
	req1.message.unknown7 = cur_session[1]-randint(0,9) #last-1
	req1.message.unknown8 = cur_session[2]-randint(0,9) #last
	req2 = stop_request.requests.add()
	req2.type = 126
	req5 = stop_request.requests.add()
	req5.type = 4
	req3 = stop_request.requests.add()
	req3.type = 129
	req4 = stop_request.requests.add()
	req4.type = 5
	req4.message.unknown4 = '05daf51635c82611d1aac95c0b051d3ec088a930' #static
	return stop_request.SerializeToString()
	
def gen_stop_data_pre(ses,cur_session):
	stop_request = pokemon_pb2.stop_request()
	stop_request.time = 2 #1
	stop_request.rpc_id = 2212820743501119519 #3 static
	#stop_request.rpc_id = generate_random_long() #3 static
	stop_request.unk1 = cur_session[1]-randint(0,9) #7
	stop_request.unk2 = cur_session[2]-randint(0,9) #8
	stop_request.unk3 = 0x4050400000000000 #9 static
	stop_request.sess.ses1 = ses.ses1 #12
	stop_request.sess.time = ses.time #12
	stop_request.sess.ses2 = ses.ses2 #12
	stop_request.unknown12 = 23229 #12 static
	
	req1 = stop_request.requests.add()
	req1.type = 104
	req1.message.unknown4 = cur_session[0]
	req1.message.unknown5 = cur_session[1]-randint(0,9)
	req1.message.unknown6 = cur_session[2]-randint(0,9)
	req2 = stop_request.requests.add()
	req2.type = 126
	req5 = stop_request.requests.add()
	req5.type = 4
	req3 = stop_request.requests.add()
	req3.type = 129
	req4 = stop_request.requests.add()
	req4.type = 5
	req4.message.unknown4 = '05daf51635c82611d1aac95c0b051d3ec088a930' #static
	return stop_request.SerializeToString()
	
def get_session(login_data):
	get_session_data = pokemon_pb2.get_session_data()
	get_session_data.ParseFromString(login_data)
	return get_session_data.requests
	
def all_stops(cur_session):
	get_all = pokemon_pb2.get_all()
	get_all.ParseFromString(base64.b64decode('CAIYjICAgNCq7pAEItABCGoSywEKogGAgICAhPzf2EeAgICAjPzf2EeAgICAlPzf2EeAgICAnPzf2EeAgICApPzf2EeAgICArPzf2EeAgICAtPzf2EeAgICAvPzf2EeAgICAxPzf2EeAgICAzPzf2EeAgICA7Pzf2EeAgICA9Pzf2EeAgICAzP/f2EeAgICA1P/f2EeAgICAhKv12UeAgICAjKv12UeAgICA9Kv12UeAgICA/Kv12UcSEgAAAAAAAAAAAAAAAAAAAAAAABkAAAAg8ddKQCEAAAAgjnMjQCICCH4iCwgEEgcIrZ3YhN8qIgMIgQEiLggFEioKKDA1ZGFmNTE2MzVjODI2MTFkMWFhYzk1YzBiMDUxZDNlYzA4OGE5MzAyqAgIBhKjCAqgCDFGrNyWNVP6ofDCGyFd07dgBPL3jUgwM0HBmBnUeUT3wdjJ8S8EjS/u1zNeATvP7qrJbavMI03JL2YFmuDLV2vu/Dur28YHrTrHMDuIWe9e1ij9ZLBFojmm090Xa9o5o+GXCZj8WL3t8LhiSnkQuj/eFJCjKQva2zqZDr94NebfMhR+bKHMW9oVX3oXxmikN4I+B7eYqNCE7jYNVTmxuzCcTTBn0ayaPNopFuRWLtHx5H3lmqGx6V87WvveGg6wTLOvL8fXEz+mzJWrWsR4EzNkLcD8LnqmD5YwmwnkNpDLUxBLpj2IsSw4xfeQTFqXYE5SXPMuS2dqXgSN4SDGpzsx1DuJ1JuS1/u9KSZRbXlpmOkBll9OpVYzURHofsvMc+Dm0nphO/A8nvUf8OSru8fj5wjoXLgqpHHna0Rql/bu4KrgyPtgUAXqy4GwGCCxCZbAMYyeR0IGjdt15+cgaVNtfK5Y75uXV8KqjhlPzOwk0wRz2HjfG2mqgBKsqfMCotLeRzUEvvx7tGrS1PPFaFF5tvzy0bf4zia+OhUW38Q7soKtM7q7c2x4QIj0Wjr5E6EzVu1EK5MAnE1apaAfIpwVVvB87hIAcsOGY35ZWWmyY7t+XM+5v/n11w3XYZvnUARLJYH/dhJucyQKHhb3jTc4A8eMy9qGMFsVfQ0TjxO3SjxEvYViG03Bm68Mak+MrhUjudXs7d5CXpscaFR4ny8CviLDZctFCc8BmDKjlxEBbGcVrnscppB3hJeX/WQIn6ACOiHcYunFOZo03lnFh2wjMoMvjuHwvl3uldhmNv6lIPoDrMWVtQcZ0obPsknkzsVfL4ImkOsiUGXLvhkGeZcttHlCiWoPhQp3rgmscmxzQRav5npbMA6nCkfMJ01K447K987pnfG4WTykBGd+zvaDdQNpjhZrgCec2Hlxde3lPu5Yc2zCpFPqT2sgAFFTAgZPaje/DMxyMbc+aWZSsK62ahSswchRSUPxkexFU9GpoiDXfTbtGhAKvzrJ2BUYarTfQI6ZlpLp+ogSR1rm+slHMgQBQBPOYx2JsqR5YtzWjPIwErvadX4YioxDwrru9lBKqUrJrD2T4GjF8sQSo6JN8j8/BBAWPPmv9hB6Gte0fXDhBeYNMAHVo/R1Bf9j1au0A05krszTs4YkmUTZ/Goye5/7ED1JWryo9noPWT6R4IT6rO+SbTBxWidJyTtsVqP0N88/bPTDX32HfK2qRXcIb/l/9qMoDKqAMzfeMM8Ro6vahDoBSN8el0DanV47/tejQ/08Wow01MaVRl6wTG9F2h174aUFlLNMLPZULqle3mSPPUWe1Bs9ysWxkjn4Rb0v7s13nwlQI4qNhew0z49vqlfOAZMbkaawyyHTNzoB8zCsD/oZje262QjBVzyEgzkAAAAg8ddKQEEAAAAgjnMjQEkAAAAAAEBQQFpbCkCjKgvMWG8aCMmLo25sgjXBCaIVUXHslYA+toR+pHvLpKGvdB7zFXE6JeYs1JghGA3dHR+wLT+U70H0iwhiOmXFELr0xYXfKhoQIz+EH5Wj/nflvemL3D3/5WDvEw=='))
	'''get_all.time = 2
	get_all.rpc_id = 8184149599452135521
	get_all.unknown12 = 8876
	get_all.unk1 = 0x404ad7f120000000
	get_all.unk2 = 0x4023738e20000000
	get_all.unk3 = 0x4050400000000000
	
	req5 = get_all.requests.add()
	req5.type = 106
	req5.message.unknown5 = 0x404ad7f120000000
	req5.message.unknown6 = 0x4023738e20000000
	
	req1 = get_all.requests.add()
	req1.type = 126
	req2 = get_all.requests.add()
	req2.type = 129
	req3 = get_all.requests.add()
	req3.type = 5
	req3.message.unknown4 = '05daf51635c82611d1aac95c0b051d3ec088a930'''
	get_all.sess.ses1 = cur_session.ses1 #12
	get_all.sess.time = cur_session.time #12
	get_all.sess.ses2 = cur_session.ses2 #12
	return get_all.SerializeToString()
	
def start_work(access_token):
	if access_token is not None:
		print '[+] Token:',access_token[:40]+'...'
		prot1=gen_first_data(access_token)
		new_api= get_api(access_token,prot1)
		login_data=use_api(new_api,prot1)
		cur_session= get_session(login_data)
		for t in found_stops:
			print '[!] farming pokestop..'
			#Kinder_pre=gen_stop_data_pre(cur_session,t)
			#use_api(new_api,Kinder_pre)
			Kinder= gen_stop_data(cur_session,t)
			use_api(new_api,Kinder)
			#print 'sleeping zzzzzZZZZZZZZ..'
			#time.sleep(4)

		#if 'Milaly432' in login_data:
		#	print '[+] logged in'
		#else:
		#	print '[-] protobuf sux..'