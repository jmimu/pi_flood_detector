#!/usr/bin/python
import os
import sys, time, random
import json
#import RPi.GPIO as GPIO

try:
  jsondata = json.load(open('/var/www/all_records.json'))
except:
  print "all_records.json not found, create a new file"
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

f_out = open('/var/www/all_records.json', 'w')
ouput=json.dumps(jsondata, sort_keys=True, separators=(',', ': '))
f_out.write(ouput)
f_out.close()

#export only last 24h for drawing

timestamp_24h_before=timestamp-24*3600*1000
jsondata_24h=[]
for measure in jsondata:
  if measure["period"]>timestamp_24h_before :
    jsondata_24h.append(measure)

f_out = open('/var/www/records24h.json', 'w')
ouput=json.dumps(jsondata_24h, sort_keys=True, separators=(',', ': '))
f_out.write(ouput)
f_out.close()
