import requests
import json

response=requests.get("http://api.open-notify.org/astros.json")
data=response.json()
print("The number of people currently in space are %d."%(data['number']))
print("They are:")
for p in data['people']:
    print("%s from %s"%(p['name'],p['craft']))
