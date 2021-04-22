import json
import urllib.request

# download raw json object
url = "http://jose167-001-site1.dtempurl.com/"
data = urllib.request.urlopen(url).read().decode()

# parse json object
obj = json.loads(data)

# output some object attributes
for value in obj:
    print("Value ->")
    print(value["value"])
