#!/usr/bin/python3

import json
import os


logfile = "/dev/shm/eHZ-EDL-MT681.log"

while True:

    os.system("/home/dietpi/bin/sml_server -s /dev/ttyUSB0 > /dev/shm/eHZ-EDL-MT681.log");

    f = open(logfile,'r')

    d = {} # create python dictionary

    for line in f:
        obis = line.strip().split('#')
        d[obis[0]] = (obis[1],obis[2])
#    print(line,end='')
#    print(line.strip().split('#'))

#    print(json.dumps(d,ensure_ascii=False))


    with open("/dev/shm/eHZ-EDL-MT681.json",'w') as fileout:
        fileout.write(json.dumps(d,ensure_ascii=False))

