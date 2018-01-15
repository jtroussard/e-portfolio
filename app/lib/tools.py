import urllib.request
import json
import logging
import datetime
from lib.config.config import *

def get_location(request):
	ip = request.environ['REMOTE_ADDR']
	try:
		with urllib.request.urlopen("https://ipapi.co/{}/json/".format(ip)) as url:
			data = json.loads(url.read().decode())
			return data
	except urllib.error.URLError as err_url:
		logging.error("[{}]tools: {}".format(datetime.datetime.now(), err_url.reason))
		return {'postal': DEFAULT_ZIP}
	except urllib.error.HTTPError as err_http:
		logging.error("[{}]tools: {}".format(datetime.datetime.now(), err_http.reason))
		return {'postal': DEFAULT_ZIP}

def get_zipcode(data):
	if not 'postal' in data:
		return DEFAULT_ZIP
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
				if distance < lowest:
					lowest = distance
					result = zip
		return result
	except urllib.error.URLError as e:
		logging.error("[{}]tools:{}".format(datetime.datetime.now(), e.reason))
		return DEFAULT_ZIP