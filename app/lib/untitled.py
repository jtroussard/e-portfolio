from flask import request
import urllib
import json

ip = request.remote_addr
print(ip)
# with urllib.request.urlopen("http://freegeoip.net/json/{}".format(ip)) as url:
#     data = json.loads(url.read().decode())
#     print(data)





from requests import get

loc = get('https://ipapi.co/json/')
print(loc.json())