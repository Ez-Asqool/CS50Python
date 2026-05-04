# Apple has its own API for their itunes service
import requests
import sys
import json #comes with python.
if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2))
#
#print(response.json()["results"][0]["trackName"])

o = response.json()
for result in o["results"]:
    print(result["trackName"])



# Go to sayings.py
