#!/usr/bin/python3

import json
import os
import paho.mqtt.client as mqtt
import random


logfile = "/dev/shm/eHZ-EDL-MT681.log"

mqttBroker ="MYBROKERIP"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
client = mqtt.Client(client_id)
client.username_pw_set(MYID, MYPWD)
client.connect(mqttBroker)

mqtt_prefix = "eHZ-EDL/"

i=0
i_max=30

power = 0.

while True:
    i=i+1
    os.system("/home/dietpi/bin/sml_server -s /dev/ttyUSB0 > /dev/shm/eHZ-EDL-MT681.log");

    f = open(logfile,'r')

    d = {} # create python dictionary
    if(i==i_max):
        for line in f:
            obis = line.strip().split('#')
            d[obis[0]] = (obis[1],obis[2])
            client.publish(mqtt_prefix + obis[0], obis[1])
        i=0
        
        power = power + (int(''.join(d["1-0:16.7.0*255"][0])))
        client.publish(mqtt_prefix + "power", power/i_max)
        power=0
    else:
        for line in f:
            obis = line.strip().split('#')
            d[obis[0]] = (obis[1],obis[2])
        power = power + (int(''.join(d["1-0:16.7.0*255"][0])))

#    print(line,end='')
#    print(line.strip().split('#'))

#    print(json.dumps(d,ensure_ascii=False))


    with open("/dev/shm/eHZ-EDL-MT681.json",'w') as fileout:
        fileout.write(json.dumps(d,ensure_ascii=False))
    
