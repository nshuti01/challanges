import json
import requests
requests.packages.urllib3.disable_warnings()

IP_ADDRESS="192.168.0.129"
INTERFACE="GigabitEthernet1"
RESTCONF_USERNAME="cisco"
RESTCONF_PASSWORD="cisco123!"


api_url = f"https://{IP_ADDRESS}/restconf/data/ietf-interfaces:interfaces/interface={INTERFACE}"
basicauth = (RESTCONF_USERNAME, RESTCONF_PASSWORD)
headers = { "Accept": "application/yang-data+json",  "Content-type":"application/yang-data+json" }


#### Step 3: Create a variable to send the request and store the JSON response
resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
#print(dir(resp))

#### Step 4: Format and display the JSON data received from the CSR1kv.
response_json = resp.json()
#print(response_json)
#print(resp.status_code)
print(resp.status_code)


