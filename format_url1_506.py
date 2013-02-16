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

if len(sys.argv) < 2:
        print "file name error"
        sys.exit(0)

filename = sys.argv[1]
print "Processing file " + filename + "..."

f1 = open("sensors.txt", 'w')
f3 = open("log", 'w')
with open(filename, 'r') as f:
        for line in f:
                line = line.rstrip()
                parts = line.split()
                raw_id = parts[0] + "_" + parts[1] + "_" + parts[2]
		# Illegal format. Skip.
		if line.find("EBU3B") < 0:
			print >> f3, "Skipping1: " + raw_id
			continue

		# find EBU3B position as temp
		temp = 3
		while temp < len(parts) and parts[temp] != 'EBU3B':
			temp+=1

		# Illegal format. Skip.
		if temp == 3 or temp >= len(parts) - 1:
			print >> f3, "Skipping2: " + raw_id
                        continue

		# type is composed of the words between uuid and EBU3B
                type1 = parts[3]
                i = 4
                while i < temp:
                        type1 += ' '
                        type1 += parts[i]
                        i+=1

		# room is after EBU3B
		room = parts[temp+1]

		# if we have a room format like "RM-3252", then we know the flooris 3. Otherwise simply use Infrastructure.
		floor = "Infrastructure"
		if room[0:2] == 'RM':
			if room[3] == 'B':
				floor = "Basement"
			else:
				floor = "Flr-" + room[3]
			room = "Rm-" + room[3:]

		status_json = json.dumps({"auth_token": auth_token, \
                            "api_key": api_key, \
                            "raw_id": raw_id, \
                            "owner":"admin@ob-ucsd-cse.ucsd.edu",\
                            "type": type1,\
                            "context":{\
                            "institution":"UCSD",\
                            "campus":"Main",\
                            "building":"EBU3B",\
                            "floor": floor,\
                            "room":room,\
                            }
                         })
		print >> f3, "Sending: id:  " + raw_id + " type: " + type1 + " floor: " + floor + " room: " + room

		try:
		    response = http.request(
		    "http://ob-ucsd-cse.ucsd.edu:8000/dataservice/api/sensors",
		    "POST",
		    status_json,
		    headers={'content-type':'application/json'}
		    )
		    print >> f1, response

		except Exception as e:
		    print "Error: ", e

print 'Creating sensors done.'
file.close(f)
file.close(f1)

filename = 'sensors.txt'
f1 = open("sensorpoints.txt", 'w')
f2 = open("urls.txt", 'w')
with open(filename, 'r') as f:
        for line in f:
                line = line.rstrip()
		if line.find("uuid") < 0:
			continue
		if line.find("name") < 0:
			continue
                parts = line.split("\"")

		temp = 0
		while temp < len(parts) and parts[temp] != 'name':
			temp+=1

		# name string is after word "name:"
		temp += 2
                name = parts[temp] + "-sp"

		while temp < len(parts) and parts[temp] != 'uuid':
			temp+=1

		# uuid string is after word "uuid:"
		temp += 2
                uuid = parts[temp]

		# Hardcode name to PresentValue
		status_json = json.dumps({"auth_token": auth_token, \
                            "api_key": api_key, \
                            "name": "PresentValue" \
                         })
		print >> f3, "Sending: " + name

		url = "http://ob-ucsd-cse.ucsd.edu:8000/dataservice/api/sensors"+ "/" + uuid + "/sensorpoints"
		print >> f2, url

		try:
		    response = http.request(
		    url,
		    "POST",
		    status_json,
		    headers={'content-type':'application/json'}
		    )
		    print >> f1, response

		except Exception as e:
		    print "Error: ", e

print 'Creating sensorpoints done.'
file.close(f)
file.close(f1)
file.close(f2)
file.close(f3)

