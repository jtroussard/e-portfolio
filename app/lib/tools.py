import urllib.request
import json
from lib.vars import *

def get_location():
	try:
		with urllib.request.urlopen("https://geoip-db.com/json") as url:
			data = json.loads(url.read().decode())
			print(data)
			return data
	except urllib.error.URLError as e:
		print(e.reason)
		return get_location()

def get_zipcode(data):
	return data['postal']

def nearest_base(data):
	lowest = 12500 # approximate circumfrence of the earth
	result = 00000 # 'winning' zipcode
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
	return result



