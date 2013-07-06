#!/usr/bin/python
import os
import sys, time, random
import json
import RPi.GPIO as GPIO

try:
  jsondata = json.load(open('/var/www/records.json'))
except:
  print "records.json not found, create a new file"
  jsondata=[]

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)
GPIO.setup(22, GPIO.IN)
coin = GPIO.input(17)
centre = GPIO.input(27)
haut = GPIO.input(22)

timestamp=int(time.time()*1000)
#~ coin=random.randint(0,1)
#~ centre=random.randint(0,1)
#~ haut=random.randint(0,1)
new_record={"period": timestamp, "coin": coin, "centre": centre, "haut":haut}

jsondata.append(new_record)

f_out = open('/var/www/records.json', 'w')
ouput=json.dumps(jsondata, sort_keys=True, separators=(',', ': '))
f_out.write(ouput)
f_out.close()
