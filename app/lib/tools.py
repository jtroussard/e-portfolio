import urllib.request
import json
import logging
from lib.vars import *

def get_location(request):
	ip = request.environ['REMOTE_ADDR']
	logging.warning("THIS IP ISSSSS -> {}".format(ip))
	try:
		with urllib.request.urlopen("https://ipapi.co/{}/json/".format(ip)) as url:
			data = json.loads(url.read().decode())
			print(data, flush=True)
			return data
	except urllib.error.URLError as err_url:
		logging.error(err_url.reason)
		return {'postal': DEFAULT_ZIP}
	except urllib.error.HTTPError as err_http:
		loggin.error(err_http.reason)
		return {'postal': DEFAULT_ZIP}


def get_zipcode(data):
	if not 'postal' in data:
		return 22193
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
				logging.info(distance)
				if distance < lowest:
					logging.info("new best zip code {}".format(zip))
					lowest = distance
					result = zip
		logging.info("best zip - {}".format(result))
		return result
	except urllib.error.URLError as e:
		logging.warning(e.reason)
		return nearest_base(data)



