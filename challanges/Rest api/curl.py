import json
import requests
requests.packages.urllib3.disable_warnings() #disable ssl certificate

api_url = "https://192.168.0.129:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity"

# dicitionary variable 
headers = { "Accept": "application/yang-data+json",
 "Content-type":"application/yang-data+json"
 }

#authenticatie
basicauth = ("cisco", "cisco123!")

#send request and store json data
resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)




#json data weergeven
print (resp.headers)
print (resp.status_code)

if resp.status_code == 200:
 print("OK")
