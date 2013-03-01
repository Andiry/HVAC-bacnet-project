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
filename1 = "bacnet_object_description_list.txt.bak"
filename2 = "bacnet_object_description_506.txt"
f3 = open("all_list.txt", 'w')

print "Processing file " + filename1 + "..."
with open(filename1, 'r') as f1:
        for line in f1:
                line = "505 " + line
		f3.write(line)

print "Processing file " + filename2 + "..."
with open(filename2, 'r') as f2:
        for line in f2:
		f3.write(line)

print 'Done.'
file.close(f1)
file.close(f2)
file.close(f3)
