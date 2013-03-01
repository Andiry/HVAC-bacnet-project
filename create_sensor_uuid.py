#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import datetime
import time
import signal
import os.path
import json
import httplib2
import urllib
import os

http = httplib2.Http()

#description_file = open('set_of_descriptions.txt', 'r')

#for line in description_file:
api_key = "5077c7d4-8c39-47c1-818f-92275d98b386"
auth_token = 2

status_json = json.dumps({"auth_token": auth_token, \
                            "api_key": api_key, \
                            "raw_id": "505_0_3000002", \
                            "owner":"admin@ob-ucsd-cse.ucsd.edu",\
                            "type":"HOT WATER DIFF PRESSURE",\
                            "context":{\
                            "institution":"UCSD",\
                            "campus":"Main",\
                            "building":"EBU3B",\
                            "floor":"HW-SYS",\
                            "room":"Infrastructure",\
                            }
                         })
print "Sending: " + status_json
try:
    response = http.request(
    "http://ob-ucsd-cse.ucsd.edu:8000/dataservice/api/sensors",
    "POST",
    status_json,
    headers={'content-type':'application/json'}
    )
    print "response: ", response

except Exception as e:
    print "Error: ", e

