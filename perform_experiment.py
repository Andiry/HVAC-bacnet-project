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

if len(sys.argv) < 4:
        print "parameter error"
        sys.exit(0)

filename = sys.argv[1]
print "Processing file " + filename + "..."

percent = string.atoi(sys.argv[2])
minute = string.atoi(sys.argv[3])

num = 0
print "Writing 3 to all rooms..."
with open(filename, 'r') as f:
	for line in f:
		line = line.rstrip()
		parts = line.split()
		raw_id = parts[1]
		uuid = parts[2]
		id1 = parts[3]
		req_url = url + uuid + "/sensorpoints/" + id1 + "/datapoints"
		print req_url
		num += 1

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

print "Writing 3 to " + num + " rooms done."

target = percent * num / 100
chosen = []

i = 0
while i < target:
        new = random.randint(0, num)
        if new not in chosen:
                chosen.append(new)
                i += 1
chosen.sort()
print "Chosen " + len(chosen) + " rooms:"
print chosen

print "Wait for one hour"
time.sleep(3600)

print "Writing 2 to " + len(chosen) + " rooms..."
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

			try:
			    response = http.request(
			    req_url,
			    "POST",
			    status_json,
			    headers={'content-type':'application/json'}
			    )
file.close(f)

print "Writing 2 to " + len(chosen) + " rooms done."
print "Wait for " + minute + " minutes"
time.sleep(60 * minute)

print "Writing 3 to " + len(chosen) + " rooms..."
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
                        print "Writing 3 to " + req_url
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

print "Writing 3 to " + len(chosen) + " rooms done."
print "Wait for one hour"
time.sleep(3600)

print "Writing -1 to all rooms..."
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
file.close(f)
print "Writing -1 to all rooms done."
