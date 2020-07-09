import requests
# import json
# Getting motion detection data from the camera
# import json
from requests.auth import HTTPDigestAuth
url = 'http://192.168.1.30/stw-cgi/eventsources.cgi?msubmenu=peoplecount&action=check'
result = requests.get(
    url,
    auth=HTTPDigestAuth('admin', '@Sapio123'),
    headers={"Accept": "application/json"})
data = result.text
print(data)
# print(type(data))
