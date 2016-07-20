import pokemon_pb2
from random import randint

def simulate_walking(ses,cur_session):
	walk = pokemon_pb2.walk()
	walk.time = 2 #1
	walk.rpc_id = 2212820743501119519-randint(0,999) #3 static
	#walk.rpc_id = generate_random_long() #3 static
	walk.unk1 = cur_session[1]#-randint(0,9) #7
	walk.unk2 = cur_session[2]#-randint(0,9) #8
	walk.unk3 = 0x4049000000000000 #9 static
	#todo
	walk.sess.ses1 = ses.session_hash #12
	walk.sess.time = ses.session_live #12
	walk.sess.ses2 = ses.session_id #12
	walk.unknown12 = randint(0,999999) #12 static
	
	req1 = walk.requests.add()
	req1.type = 106
	req1.message.unknown6 = cur_session[1]#-randint(0,9)
	req1.message.unknown7 = cur_session[2]#-randint(0,9)
	req2 = walk.requests.add()
	req2.type = 126
	req5 = walk.requests.add()
	req5.type = 4
	req3 = walk.requests.add()
	req3.type = 129
	req4 = walk.requests.add()
	req4.type = 5
	req4.message.unknown4 = '05daf51635c82611d1aac95c0b051d3ec088a930' #static
	return walk.SerializeToString()
	
def gen_stop_data_pre(ses,cur_session):
	stop_request = pokemon_pb2.stop_request()
	stop_request.time = 2 #1
	stop_request.rpc_id = 2212820743501119519-randint(0,999) #3 static
	#stop_request.rpc_id = generate_random_long() #3 static
	stop_request.unk1 = cur_session[1]#-randint(0,9) #7
	stop_request.unk2 = cur_session[2]#-randint(0,9) #8
	stop_request.unk3 = 0x4049000000000000 #9 static
	stop_request.sess.ses1 = ses.session_hash #12
	stop_request.sess.time = ses.session_live #12
	stop_request.sess.ses2 = ses.session_id #12
	stop_request.unknown12 = randint(0,999999) #12 static
	
	req1 = stop_request.requests.add()
	req1.type = 104
	req1.message.unknown4 = cur_session[0]
	req1.message.unknown5 = cur_session[1]#-randint(0,9)
	req1.message.unknown6 = cur_session[2]#-randint(0,9)
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
	
def all_stops(cur_session):
	get_all = pokemon_pb2.get_all()
	get_all.ParseFromString(base64.b64decode('CAIYjICAgNCq7pAEItABCGoSywEKogGAgICAhPzf2EeAgICAjPzf2EeAgICAlPzf2EeAgICAnPzf2EeAgICApPzf2EeAgICArPzf2EeAgICAtPzf2EeAgICAvPzf2EeAgICAxPzf2EeAgICAzPzf2EeAgICA7Pzf2EeAgICA9Pzf2EeAgICAzP/f2EeAgICA1P/f2EeAgICAhKv12UeAgICAjKv12UeAgICA9Kv12UeAgICA/Kv12UcSEgAAAAAAAAAAAAAAAAAAAAAAABkAAAAg8ddKQCEAAAAgjnMjQCICCH4iCwgEEgcIrZ3YhN8qIgMIgQEiLggFEioKKDA1ZGFmNTE2MzVjODI2MTFkMWFhYzk1YzBiMDUxZDNlYzA4OGE5MzAyqAgIBhKjCAqgCDFGrNyWNVP6ofDCGyFd07dgBPL3jUgwM0HBmBnUeUT3wdjJ8S8EjS/u1zNeATvP7qrJbavMI03JL2YFmuDLV2vu/Dur28YHrTrHMDuIWe9e1ij9ZLBFojmm090Xa9o5o+GXCZj8WL3t8LhiSnkQuj/eFJCjKQva2zqZDr94NebfMhR+bKHMW9oVX3oXxmikN4I+B7eYqNCE7jYNVTmxuzCcTTBn0ayaPNopFuRWLtHx5H3lmqGx6V87WvveGg6wTLOvL8fXEz+mzJWrWsR4EzNkLcD8LnqmD5YwmwnkNpDLUxBLpj2IsSw4xfeQTFqXYE5SXPMuS2dqXgSN4SDGpzsx1DuJ1JuS1/u9KSZRbXlpmOkBll9OpVYzURHofsvMc+Dm0nphO/A8nvUf8OSru8fj5wjoXLgqpHHna0Rql/bu4KrgyPtgUAXqy4GwGCCxCZbAMYyeR0IGjdt15+cgaVNtfK5Y75uXV8KqjhlPzOwk0wRz2HjfG2mqgBKsqfMCotLeRzUEvvx7tGrS1PPFaFF5tvzy0bf4zia+OhUW38Q7soKtM7q7c2x4QIj0Wjr5E6EzVu1EK5MAnE1apaAfIpwVVvB87hIAcsOGY35ZWWmyY7t+XM+5v/n11w3XYZvnUARLJYH/dhJucyQKHhb3jTc4A8eMy9qGMFsVfQ0TjxO3SjxEvYViG03Bm68Mak+MrhUjudXs7d5CXpscaFR4ny8CviLDZctFCc8BmDKjlxEBbGcVrnscppB3hJeX/WQIn6ACOiHcYunFOZo03lnFh2wjMoMvjuHwvl3uldhmNv6lIPoDrMWVtQcZ0obPsknkzsVfL4ImkOsiUGXLvhkGeZcttHlCiWoPhQp3rgmscmxzQRav5npbMA6nCkfMJ01K447K987pnfG4WTykBGd+zvaDdQNpjhZrgCec2Hlxde3lPu5Yc2zCpFPqT2sgAFFTAgZPaje/DMxyMbc+aWZSsK62ahSswchRSUPxkexFU9GpoiDXfTbtGhAKvzrJ2BUYarTfQI6ZlpLp+ogSR1rm+slHMgQBQBPOYx2JsqR5YtzWjPIwErvadX4YioxDwrru9lBKqUrJrD2T4GjF8sQSo6JN8j8/BBAWPPmv9hB6Gte0fXDhBeYNMAHVo/R1Bf9j1au0A05krszTs4YkmUTZ/Goye5/7ED1JWryo9noPWT6R4IT6rO+SbTBxWidJyTtsVqP0N88/bPTDX32HfK2qRXcIb/l/9qMoDKqAMzfeMM8Ro6vahDoBSN8el0DanV47/tejQ/08Wow01MaVRl6wTG9F2h174aUFlLNMLPZULqle3mSPPUWe1Bs9ysWxkjn4Rb0v7s13nwlQI4qNhew0z49vqlfOAZMbkaawyyHTNzoB8zCsD/oZje262QjBVzyEgzkAAAAg8ddKQEEAAAAgjnMjQEkAAAAAAEBQQFpbCkCjKgvMWG8aCMmLo25sgjXBCaIVUXHslYA+toR+pHvLpKGvdB7zFXE6JeYs1JghGA3dHR+wLT+U70H0iwhiOmXFELr0xYXfKhoQIz+EH5Wj/nflvemL3D3/5WDvEw=='))
	'''get_all.time = 2
	get_all.rpc_id = 8184149599452135521
	get_all.unknown12 = 8876
	get_all.unk1 = 0x404ad7f120000000
	get_all.unk2 = 0x4023738e20000000
	get_all.unk3 = 0x4049000000000000
	
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
	
def gen_stop_data(ses,cur_session):
	stop_request = pokemon_pb2.stop_request()
	stop_request.time = 2 #1
	#stop_request.rpc_id = 9077956684869009422 #3 static
	stop_request.rpc_id = 2212820743501119519-randint(0,999) #3 static
	stop_request.unk1 = cur_session[1]#-randint(0,9) #7
	stop_request.unk2 = cur_session[2]#-randint(0,9) #8
	stop_request.unk3 = 0x4049000000000000 #9 static
	stop_request.unknown12 = randint(0,999999) #12 static
	stop_request.sess.ses1 = ses.session_hash #12
	stop_request.sess.time = ses.session_live #12
	stop_request.sess.ses2 = ses.session_id #12
	
	req1 = stop_request.requests.add()
	req1.type = 101
	req1.message.unknown4 = cur_session[0]
	req1.message.unknown5 = cur_session[1]#-randint(0,9)
	req1.message.unknown6 = cur_session[2]#-randint(0,9)
	req1.message.unknown7 = cur_session[1]#-randint(0,9) #last-1
	req1.message.unknown8 = cur_session[2]#-randint(0,9) #last
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
	
def gen_first_data(access_token):
	login_request = pokemon_pb2.login_request()
	login_request.time = 2
	login_request.unknown12 = randint(0,999999)
	login_request.rpc_id = 72185515343874-randint(0,999)
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
	
	