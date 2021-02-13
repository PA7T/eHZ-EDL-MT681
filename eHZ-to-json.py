#!/usr/bin/python3

import json
import os
import paho.mqtt.client as mqtt
import random

logfile = "/dev/shm/eHZ-EDL-MT681.log"

mqttBroker ="BROKERIP"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
client = mqtt.Client(client_id)
client.username_pw_set(MYUSERNAME, MYPASSWORD)
client.connect(mqttBroker)

mqtt_prefix = "eHZ-EDL/"

while True:

    os.system("/home/dietpi/bin/sml_server -s /dev/ttyUSB0 > /dev/shm/eHZ-EDL-MT681.log");

    f = open(logfile,'r')

    d = {} # create python dictionary

    for line in f:
        obis = line.strip().split('#')
        d[obis[0]] = (obis[1],obis[2])
        client.publish(mqtt_prefix + obis[0], obis[1])
#    print(line,end='')
#    print(line.strip().split('#'))

#    print(json.dumps(d,ensure_ascii=False))


    with open("/dev/shm/eHZ-EDL-MT681.json",'w') as fileout:
        fileout.write(json.dumps(d,ensure_ascii=False))

