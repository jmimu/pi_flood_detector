With Raspian

help with RPi GPIO : http://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/

install python libs:

sudo apt-get update && sudo apt-get upgrade
sudo apt-get install python-smbus ipython python-cwiid python-scipy python-numpy python-pygame python-setuptools libsdl-dev
sudo aptitude install python-pip
sudo pip install rpi.gpio

to get some space:
dpkg-query -W --showformat='${Installed-Size;10}\t${Package}\n' | sort -k1,1n
sudo aptitude remove omxplayer gnome-icon-theme gnome-accessibility-themes gnome-themes-standard-data gnome-themes-standard midori scratch smbclient desktop-base
(about 125MB)

install apache server: (see http://my-music.mine.nu/images/rpi_raspianwheezy_setup.pdf)

sudo aptitude install apache2

copy index.html, lib/ and read_flood_sensor.py to /var/www

add it to cron:
crontab -e

add line:
0,10,20,30,40,50 * * * * /var/www/read_flood_sensor.py


Enable port forwarding on your router.


make sensor: see sensors folder.


TODO:
make a new json file for every day, to keep a record and display only last values?
