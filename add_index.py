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
filename1 = sys.argv[1]
f3 = open(filename1 + "-indexed", 'w')

print "Processing file " + filename1 + "..."
i = 0;
with open(filename1, 'r') as f1:
        for line in f1:
                line = str(i) + "	" + line
		f3.write(line)
		i+=1

print 'Done.'
file.close(f1)
file.close(f3)
