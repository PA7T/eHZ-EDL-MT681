#!/usr/bin/python3

import json

logfile = "/dev/shm/eHZ-EDL-MT681.log"

f = open(logfile,'r')

d = {} # create python dictionary

for line in f:
    obis = line.strip().split('#')
    d[obis[0]] = (obis[1],obis[2])
#    print(line,end='')
#    print(line.strip().split('#'))

print(json.dumps(d,ensure_ascii=False))
