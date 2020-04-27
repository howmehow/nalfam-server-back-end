import requests
import json
import datetime
import random
response = requests.get('http://localhost:5000/devices/')
devices = response.json()
# packages = json.dumps(data, indent=2)
for device in devices:
    device['timeStamp'] = str(datetime.datetime.now()).split('.')[0]
    device['upload'] = random.getrandbits(10)
    device['download'] = random.getrandbits(20)
jason = json.dumps(devices, indent=2)
# print(devices)
print(jason)
#TODO add jason to sql 


# packages=json.loads(data)
# time = datetime.now()
# for package in packages:
#     package["TimeStamp"] = time

# print(packages)
