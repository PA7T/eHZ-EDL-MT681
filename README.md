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
## clone git repository
```bash
git clone https://github.com/PA7T/eHZ-EDL-MT681.git
```
## copy files to their location
```bash
cd eHZ-EDL-MT681
cp eHZ-to-json.py /home/dietpi/bin/
cp MT681_daemon.sh /home/dietpi/bin/
sudo cp mt681.service /etc/systemd/system/
```

## start and enable daemon to monitor eHZ-EDL MT681 serial output
```bash
sudo systemctl start mt681
sudo systemctl enable mt681
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
http://dietpi.local/
