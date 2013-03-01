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

f1 = open("test_urls.txt", 'r')
f2 = open("results.txt", 'w')
f3 = open("time.txt", 'w')
for line in f1:
	line = line.rstrip()
	parts = line.split(" ")
	uuid = parts[1] 
	url1 = "http://ob-ucsd-cse.ucsd.edu:8000/dataservice/api/sensors/" + uuid + "/sensorpoints"
	try:
	    response = http.request(
	    url1,
	    "GET",
	    headers={"X-BD-Api-Key": api_key, "X-BD-Auth-Token": auth_token}
	    )
	    print >> f2, response

	except Exception as e:
	    print "Error: ", e

	response = str(response)
	response = response.rstrip()
	parts1 = response.split("\"")

	temp = 0
	while temp < len(parts1) and parts1[temp] != 'id':
		temp+=1

	key_id = parts1[temp+1]
	key_id = key_id[1:7]

	times = []
	url2 = "http://ob-ucsd-cse.ucsd.edu:8000/dataservice/api/sensors/" + uuid + "/sensorpoints/" + key_id + "/datapoints" 
	i = 0
	while i < 10:
		start = time.time()
		try:
		    response = http.request(
		    url2,
		    "GET",
		    headers={"X-BD-Api-Key": api_key, "X-BD-Auth-Token": auth_token}
		    )
		    end = time.time()
		    print >> f2, response
		    print >> f2, end - start

		except Exception as e:
		    end = time.time()
		    print "Error: ", e

		times.append(float(end - start))
		i+=1

	print >> f2, times

	i = 0
	sum = 0
	while i < 10:
		sum += times[i]
		i += 1 
	print >> f3, sum / 10

print 'done.'
file.close(f1)
file.close(f2)
file.close(f3)
