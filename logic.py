import pokemon_pb2
from random import randint
import location
import base64
from google.protobuf.internal import encoder
from s2sphere import *
from binascii import unhexlify

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
	
def encode(cellid):
	output = []
	encoder._VarintEncoder()(output.append, cellid)
	return ''.join(output)
	
def getNeighbors():
	origin = CellId.from_lat_lng(LatLng.from_degrees(location.FLOAT_LAT , location.FLOAT_LONG)).parent(15)
	walk = [origin.id()]
	# 10 before and 10 after
	next = origin.next()
	prev = origin.prev()
	for i in range(10):
		walk.append(prev.id())
		walk.append(next.id())
		next = next.next()
		prev = prev.prev()
	return walk
	
def all_stops(cur_session):
	get_all = pokemon_pb2.get_all()
	walk = sorted(getNeighbors())	
	get_all.unk1=2
	get_all.unk3=2212820743501119519-randint(0,999)
	get_all.unk12=randint(0,999999)
	lat,lon,fl=location.get_location_coords()

	req1 = get_all.b.add()	
	req1.id = 106
	req1.c.msg=''.join(map(encode, walk))
	req1.c.lat=lat
	req1.c.lon=lon
	req2 = get_all.b.add()
	req2.id = 126
	req5 = get_all.b.add()
	req5.id = 4
	req3 = get_all.b.add()
	req3.id = 129
	req4 = get_all.b.add()
	req4.id = 5
	req4.c.msg = '05daf51635c82611d1aac95c0b051d3ec088a930' #static
	
	get_all.sess.session_hash = cur_session.ses.session_hash #12
	get_all.sess.session_live = cur_session.ses.session_live #12
	get_all.sess.session_id = cur_session.ses.session_id #12
	get_all.unk7=lat
	get_all.unk8=lon
	get_all.unk9=0x4049000000000000
	return get_all.SerializeToString()
	
def gen_stop_data(ses,cur_session):
	stop_request = pokemon_pb2.stop_request()
	stop_request.time = 2 #1
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
	location.set_location_coords(location.l2f(cur_session[1]),location.l2f(cur_session[2]),location.l2f(0x4049000000000000))
	return stop_request.SerializeToString()
	
def gen_first_data(access_token,ltype):
	login_request = pokemon_pb2.login_request()
	login_request.time = 2
	login_request.unknown12 = randint(0,999999)
	login_request.rpc_id = 72185515343874-randint(0,999)
	login_request.auth.provider = ltype
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
	
def long_to_bytes (val, endianness='big'):
	"""
	Use :ref:`string formatting` and :func:`~binascii.unhexlify` to
	convert ``val``, a :func:`long`, to a byte :func:`str`.

	:param long val: The value to pack

	:param str endianness: The endianness of the result. ``'big'`` for
	  big-endian, ``'little'`` for little-endian.

	If you want byte- and word-ordering to differ, you're on your own.

	Using :ref:`string formatting` lets us use Python's C innards.
	"""

	# one (1) hex digit per four (4) bits
	width = val.bit_length()

	# unhexlify wants an even multiple of eight (8) bits, but we don't
	# want more digits than we need (hence the ternary-ish 'or')
	width += 8 - ((width % 8) or 8)

	# format width specifier: four (4) bits per hex digit
	fmt = '%%0%dx' % (width // 4)

	# prepend zero (0) to the width, to zero-pad the output
	s = unhexlify(fmt % val)

	if endianness == 'little':
		# see http://stackoverflow.com/a/931095/309233
		s = s[::-1]

	return s
	
def catch_it(ses,cur_session):
	#cur_session (21, 4632737554732154986L, 4621790981467132021L, u'47b185ff63b', 10215399323137525133L, 86.69675826461956)
	stop_requests = pokemon_pb2.stop_requests()
	stop_requests.time = 2 #1
	stop_requests.rpc_id = 2212820743501119519-randint(0,999) #3 static
	#stop_requests.unk1 = cur_session[1]#-randint(0,9) #7
	stop_requests.unk1 = location.get_lat()#-randint(0,9) #7
	#stop_requests.unk2 = cur_session[2]#-randint(0,9) #8
	stop_requests.unk2 = location.get_lot()#-randint(0,9) #8
	stop_requests.unk3 = 0x4049000000000000 #9 static
	stop_requests.unknown12 = randint(0,999999) #12 static
	stop_requests.sess.ses1 = ses.session_hash #12
	stop_requests.sess.time = ses.session_live #12
	stop_requests.sess.ses2 = ses.session_id #12
	
	req1 = stop_requests.requests.add()
	m1 = pokemon_pb2.stop_requests.Requests()
	m1.type = 143
	#req1.message.unknown4 = long_to_bytes(cur_session[4])
	#m = pokemon_pb2.RequestEnvelop.Unknown9()
	m = pokemon_pb2.stop_requests.Unknown9()
	#req1.message.unknown4 = cur_session[4]
	#req1.message.unknown5 = 1#-randint(0,9)
	#req1.message.unknown6 = 0x3ff1c8dcc0000000#-randint(0,9)
	#req1.message.unknown7 = cur_session[3]#-randint(0,9) #last-1
	#req1.message.unknown8 = 1#-randint(0,9) #last
	#req1.message.unknown9 = 0x3f35c54100000000#-randint(0,9) #last
	#req1.message.unknown10 = 0x3ff0000000000000#-randint(0,9) #last
	
	m.unknown4 = cur_session[4]
	m.unknown5 = cur_session[3]#-randint(0,9)
	#m.unknown5 = 1#-randint(0,9)
	#m.unknown6 = 0x4000000000000000#-randint(0,9)
	#m.unknown7 = cur_session[3]#-randint(0,9) #last-1
	#m.unknown8 = 1#-randint(0,9) #last
	#m.unknown9 = 0x3f35c54100000000#-randint(0,9) #last
	#m.unknown10 = 0x3ff0000000000000#-randint(0,9) #last
	m1.message = m.SerializeToString()
	req1.MergeFrom(m1)
	
	req2 = stop_requests.requests.add()
	req2.type = 126
	req5 = stop_requests.requests.add()
	req5.type = 4
	req3 = stop_requests.requests.add()
	req3.type = 129
	req4 = stop_requests.requests.add()
	req4.type = 5
	req4.MergeFrom(m5)
	m5 = pokemon_pb2.stop_requests.Requests()
	m = pokemon_pb2.stop_requests.MessageSingleString()
	m.bytes = "05daf51635c82611d1aac95c0b051d3ec088a930"
	m5.message = m.SerializeToString()
	
	req6 = stop_requests.requests.add()
	req6.type =142
	m = pokemon_pb2.stop_requests.MessageSingleString()
	m.unknown1=
	m.unknown2=
	
	#req4.message.unknown4 = '05daf51635c82611d1aac95c0b051d3ec088a930' #static
	#location.set_location_coords(location.l2f(cur_session[1]),location.l2f(cur_session[2]),location.l2f(0x4049000000000000))
	return stop_requests.SerializeToString()