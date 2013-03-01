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
status_json = json.dumps({"auth_token": 1, "api_key": 1, "stream":[{"datapoint": 5, "occurred": "2013-01-25T16:11:48.673556-08:00"}]})
print "Sending: " + status_json
try:
    response = http.request(
    #"http://localhost:8080/se/demo/sniffer/postUpdates",
    "http://ob-ucsd-cse.ucsd.edu:8000/dataservice/api/sensors/example-sensor-4/sensorpoints/10004/datapoints",
    "POST",
    status_json,
    #headers={'content-type':'text/plain'}
    headers={'content-type':'application/json'}
    )
    print "response: ", response

except Exception as e:
    print "Error: ", e

