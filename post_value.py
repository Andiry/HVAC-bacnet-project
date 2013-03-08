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
auth_token = "2"

url = "http://ob-ucsd-cse.ucsd.edu:8000/dataservice/api/sensors/"

if len(sys.argv) < 2:
        print "file name error"
        sys.exit(0)

filename = sys.argv[1]
print "Processing file " + filename + "..."

with open(filename, 'r') as f:
	for line in f:
		line = line.rstrip()
		parts = line.split()
		raw_id = parts[1]
		uuid = parts[2]
		id1 = parts[3]
		req_url = url + uuid + "/sensorpoints/" + id1 + "/datapoints"
		print req_url

		status_json = json.dumps({"auth_token": auth_token, \
                            "api_key": api_key, \
                            "raw_id": raw_id, \
                            "stream": [\
                            {\
			    "datapoint": 3,\
                            "occurred:": datetime.datetime.now().strftime("%Y-%m-%dT%X.%f-08:00")\
                            }\
			    ]\
                         })

		try:
		    response = http.request(
		    req_url,
		    "POST",
		    status_json,
		    headers={'content-type':'application/json'}
		    )


file.close(f)
