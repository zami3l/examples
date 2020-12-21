#!/usr/bin/env python
# coding: utf-8

import requests

TARGET = "10.10.235.223"
PORT = "8000"

# Send and view result
def REQ(target, port, additionalPath):
    return requests.get('http://{}:{}{}'.format(target, port, additionalPath)).text

# Test key API (The key is between 0 and 100 and is odd)
for key_api in range(1, 100, 2):

    pathAPI = "/api/{}".format(key_api)
    print(REQ(TARGET, PORT, pathAPI))