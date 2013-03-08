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

percentage = string.atoi(sys.argv[2])
minute = string.atoi(sys.argv[3])

num = 0
with open(filename, 'r') as f:
	for line in f:
		line = line.rstrip()
		parts = line.split()
		raw_id = parts[1]
		uuid = parts[2]
		id1 = parts[3]
		req_url = url + uuid + "/sensorpoints/" + id1 + "/datapoints"
		print req_url
		print datetime.datetime.now().strftime("%Y-%m-%dT%X.%f-08:00")
		num += 1
file.close(f)

print num
target = percentage * num /100
print target
print percentage + minute

chosen = []
i = 0
while i < target:
	new = random.randint(0, num)
	if new not in chosen:
		chosen.append(new)
		i += 1
chosen.sort()
print chosen
print len(chosen)

time.sleep(10)
with open(filename, 'r') as f:
	for line in f:
		line = line.rstrip()
		parts = line.split()
		index = string.atoi(parts[0])
		if index in chosen:
			print line
file.close(f)
