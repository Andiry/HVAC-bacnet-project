#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import datetime
import time
import signal
import string
import os.path
import json
import httplib2
import urllib
import os
import random

http = httplib2.Http()

#description_file = open('set_of_descriptions.txt', 'r')

#for line in description_file:
api_key = "5077c7d4-8c39-47c1-818f-92275d98b386"
auth_token = "2"

url = "http://ob-ucsd-cse.ucsd.edu:8000/dataservice/api/sensors/"

if len(sys.argv) < 2:
        print "parameter error"
        sys.exit(0)

filename = sys.argv[1]
print "Processing file " + filename + "..."

#percent = string.atoi(sys.argv[2])
#minute = string.atoi(sys.argv[3])

num = 0
with open(filename, 'r') as f:
	for line in f:
		num += 1
file.close(f)

#target = percent * num / 100
target = 1
chosen = []

i = 0
while i < target:
        new = random.randint(0, num)
        if new not in chosen:
                chosen.append(new)
                i += 1
chosen.sort()
print "Chosen " + str(len(chosen)) + " rooms:"
print chosen

print "Writing 2 to " + str(len(chosen)) + " rooms..."
with open(filename, 'r') as f:
        for line in f:
                line = line.rstrip()
                parts = line.split()
                index = string.atoi(parts[0])
                if index in chosen:
			raw_id = parts[1]
			uuid = parts[2]
			id1 = parts[3]
			req_url = url + uuid + "/sensorpoints/" + id1 + "/datapoints"
                        print "Writing 2 to " + req_url

			status_json = json.dumps({"auth_token": auth_token, \
                            "api_key": api_key, \
                            "raw_id": raw_id, \
                            "stream": [\
                            {\
			    "datapoint": 2,\
                            "occurred:": datetime.datetime.now().strftime("%Y-%m-%dT%X.%f-08:00")\
                            }\
			    ]\
                        })

			start = time.time()
			try:
			    response = http.request(
			    req_url,
			    "POST",
			    status_json,
			    headers={'content-type':'application/json'}
			    )
			except Exception as e:
                	    print "Error: ", e

file.close(f)
print "Writing 2 to " + str(len(chosen)) + " rooms done."

print "Checking status"
api_key_new = "84a96fad-1aa7-4c05-aeeb-286b781584b0"
req_url = "http://ob-ucsd-cse.ucsd.edu:8000/dataservice/api/subscribers/bacnet_connector@ob-ucsd-cse.ucsd.edu/changes"

while 1:
	try:
	    response = http.request(
	    req_url, 
	   "GET",
	    headers={"X-BD-Api-Key": api_key_new, "X-BD-Auth-Token": auth_token}
	    )
	except Exception as e:
	    print "Error: ", e

	print response
	response = str(response)
	response = response.rstrip()
	parts = response.split("\"")

	temp = 0
	while temp < len(parts) and parts[temp] != 'data':
		temp+=1

	if temp < len(parts):
		id1 = parts[temp+2]

	if id1 == 'links':
		break

end = time.time()
print end - start

print "Writing -1 to " + str(len(chosen)) + " rooms..."
with open(filename, 'r') as f:
        for line in f:
                line = line.rstrip()
                parts = line.split()
                index = string.atoi(parts[0])
                if index in chosen:
			raw_id = parts[1]
			uuid = parts[2]
			id1 = parts[3]
			req_url = url + uuid + "/sensorpoints/" + id1 + "/datapoints"
                        print "Writing -1 to " + req_url

			status_json = json.dumps({"auth_token": auth_token, \
                            "api_key": api_key, \
                            "raw_id": raw_id, \
                            "stream": [\
                            {\
			    "datapoint": -1,\
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
			except Exception as e:
                	    print "Error: ", e

file.close(f)
