import pokemon_pb2
import base64

def main():
	session_606=base64.b64decode('CDUQgoCAgPC0EBojcGdvcmVsZWFzZS5uaWFudGljbGFicy5jb20vcGxmZS8yODc6WwpAiDg94fT5Xz+SrN1aav/hmoiB2GiZivMy5SvjIlWJ53f0r9gqBYk92sB3sLjg3tzwp99VOYZhIC8PazFWQkJy2xDxiryk3yoaEKG6fV3bm5peRTDQXJfZ722iBgA=')
	get_session_data = pokemon_pb2.get_session_data()
	get_session_data.ParseFromString(session_606)
	print get_session_data

if __name__ == '__main__':
	main()