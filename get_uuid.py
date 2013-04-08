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

url = "http://ob-ucsd-cse.ucsd.edu:8000/dataservice/api/sensors/context/raw_id="

if len(sys.argv) < 2:
        print "file name error"
        sys.exit(0)

filename = sys.argv[1]
print "Processing file " + filename + "..."

f1 = open("uuid-occupy-room.txt", 'w')
with open(filename, 'r') as f:
	for line in f:
		line = line.rstrip()
		parts = line.split()
		raw_id = parts[0] + "_" + parts[1] + "_" + parts[2]
		room = parts[6]
		room = room[3:]
		req_url = url + raw_id

		try:
		    response = http.request(
		    req_url, 
		   "GET",
		    headers={"X-BD-Api-Key": api_key, "X-BD-Auth-Token": auth_token}
		    )

		except Exception as e:
		    print "Error: ", e

		response = str(response)
		response = response.rstrip()
		parts = response.split("\"")

		temp = 0
		while temp < len(parts) and parts[temp] != 'uuid':
			temp+=1

		if temp < len(parts):
			uuid = parts[temp+2]

		line = room + " " + raw_id + " " + uuid + "\n"

		url1 = "http://ob-ucsd-cse.ucsd.edu:8000/dataservice/api/sensors/" + uuid + "/sensorpoints"
		try:
		    response = http.request(
		    url1, 
		   "GET",
		    headers={"X-BD-Api-Key": api_key, "X-BD-Auth-Token": auth_token}
		    )

		except Exception as e:
		    print "Error: ", e

		response = str(response)
		response = response.rstrip()
		parts = response.split("\"")

		temp = 0
		while temp < len(parts) and parts[temp] != 'id':
			temp+=1

		if temp < len(parts):
			id1 = parts[temp+1]

		id1 = id1[1:7]
		line = room + " " + raw_id + " " + uuid + " " + id1 + "\n"
		print line
		f1.write(line)

file.close(f)
file.close(f1)
