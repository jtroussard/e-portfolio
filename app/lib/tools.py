import urllib.request
import json
from lib.vars import *

def get_location(request):
	ip = request.environ['REMOTE_ADDR']
	print("THIS IP ISSSSS -> {}".format(ip))
	try:
		with urllib.request.urlopen("https://ipapi.co/{}/json/".format(ip)) as url:
			data = json.loads(url.read().decode())
			print(data)
			return data
	except urllib.error.URLError as err_url:
		print(err_url.reason)
		return get_location()
	except urllib.error.HTTPError as err_http:
		print(err_http.reason)
		return {'postal': DEFAULT_ZIP}


def get_zipcode(data):
	return data['postal']

def nearest_base(data):
	lowest = 12500 # approximate circumfrence of the earth
	result = 00000 # 'winning' zipcode
	try:
		for zip in HOMEBASES:
			url = "https://www.zipcodeapi.com/rest/{}/distance.{}/{}/{}/{}".format(
				ZIP_API_KEY, ZIP_FORMAT, zip, data, ZIP_UNIT)
			with urllib.request.urlopen(url) as r_json:
				distance =  json.loads(r_json.read().decode())['distance']
				print(distance)
				if distance < lowest:
					print("new best zip code {}".format(zip))
					lowest = distance
					result = zip
		print("best zip - {}".format(result))
		return result
	except urllib.error.URLError as e:
		print(e.reason)
		return nearest_base(data)



