import logic
import stops
import api
import time
import pokemon_pb2

def start_private_show(access_token,ltype):
	print '[+] Token:',access_token[:40]+'...'
	prot1=logic.gen_first_data(access_token)
	local_ses=api.get_rpc_server(access_token,prot1)
	while(local_ses is not None):
		print '[+] starting show'
		for t in stops.get_static():
			#small_show(t,access_token,local_ses)
			print '[!] farming pokestop..'
			new_rcp_point='https://%s/rpc'%(local_ses.rpc_server,)
			work_with_stops(t,local_ses.ses,new_rcp_point)
	#prot1=logic.gen_first_data(access_token)
	#sid= get_rpc_server(access_token,prot1)
	#new_rcp_point='https://%s/rpc'%(sid.rpc_server,)
	#login_data=use_api(new_rcp_point,prot1)
	#if sid is not None:
	#	for t in stops.get_static():
	#		print '[!] farming pokestop..'
	#		work_with_stops(t,sid.ses,new_rcp_point)
			#walking=logic.simulate_walking(ses,t)
			#use_api(new_rcp_point,walking)
			#time.sleep(1)
			#Kinder_pre=logic.gen_stop_data_pre(ses,t)
			#use_api(new_rcp_point,Kinder_pre)
			#time.sleep(1)
			
def work_with_stops(current_stop,ses,new_rcp_point):
	Kinder= logic.gen_stop_data(ses,current_stop)
	tmp_api=api.use_api(new_rcp_point,Kinder)
	if tmp_api is not None:
		map = pokemon_pb2.map()
		map.ParseFromString(tmp_api)
		#print map
		st= map.sess[0].status
		if st==4:
			print "[!] +%s"%map.sess[0].amt
		elif st==3:
			print "[!] used"
		elif st==2:
			print "[!] charging"
		elif st==1:
			print "[!] teleport.."
			time.sleep(5)
			work_with_stops(current_stop,ses,new_rcp_point)
		else:
			print "[?]:",st
		time.sleep(2)
	else:
		print '[-] tmp_api empty'