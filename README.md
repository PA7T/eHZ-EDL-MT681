# eHZ-EDL-MT681
Dietpi installation for eHZ-EDL-MT681 smart meter language parsing

# Install DietPi

# Install additional packages

INSTALL lighthttpd via dietpi-software

sudo apt-get install vim screen git uuid-dev uuid-runtime
sudo dietpi-software install 16 # build essentials

# Customise installation

## install libsml: smart meter language parser
```bash
mkdir bin
mkdir src
cd src
git clone https://github.com/volkszaehler/libsml.git
cd libsml
make
cp examples/sml_server /home/dietpi/bin
```

## install eHZ-to-json.py
cp eHZ-to-json.py /home/dietpi/bin/eHZ-to-json.py

# edit cron with:  crontab -e
```bash
* * * * * /home/dietpi/bin/sml_server -s /dev/ttyUSB0 > /dev/shm/eHZ-EDL-MT681.log; python3 /home/dietpi/bin/eHZ-to-json.py > /dev/shm/eHZ-EDL-MT681.json
```

# make link to date for webserver access
```bash
cd /var/www
sudo ln -s /dev/shm/eHZ-EDL-MT681.json eHZ-EDL-MT681.json
```

# access data
http://dietpi.local/eHZ-EDL-MT681.json

# display data via webserver
place index.html in /var/www/
