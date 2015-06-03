#!/usr/bin/env python

import httplib2
import serial

ser = serial.Serial('/dev/ttyUSB0', 57600)
isParked = "1"
a = 0
last_isParked = 0

while 1 :
        ch = ser.read(1)
        if ch == '\n':
                print isParked
                a = int(isParked)
                conn = httplib2.Http()
                conn.request("http://api.thingspeak.com/update?key=ZZS51FEPXME4SKN6&field1=%d" %(a))
                isParked = ''
        else:
                isParked += ch

