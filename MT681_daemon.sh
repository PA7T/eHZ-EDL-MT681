#!/bin/bash

while true
do

  /home/dietpi/bin/sml_server -s /dev/ttyUSB0 > /dev/shm/eHZ-EDL-MT681.log
  python3 /home/dietpi/bin/eHZ-to-json.py > /dev/shm/eHZ-EDL-MT681.json

done
