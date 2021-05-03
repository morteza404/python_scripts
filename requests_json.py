#!/usr/bin/env python3

import requests
from pprint import pprint

URL = "http://ip-api.com/json/"

response = requests.get(URL)

pprint(response.json())