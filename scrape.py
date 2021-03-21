# skeleton for your optional challenge

import requests
import time
from pprint import pprint

# get a token here: https://aqicn.org/data-platform/token/#/
token = "demo" # FILL IN HERE

while True:
    url = f"http://api.waqi.info/feed/shanghai/?token={token}"
    res = requests.get(url)
    pprint(res.json()['data'])
    time.sleep(5)

    # you will need to hook it up to an HTTP server
    # you may refer to ./server.py for an example
    # or if you prefer, you can use a framework such as Flask
