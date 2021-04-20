#! /usr/bin/python3

import serial, time, sys, json
from datetime import datetime

baud_rate = 9600  #  In arduino, Serial.begin(baud_rate), e.g. 115200
default = time.strftime("log_%Y%m%d_%H%M.txt")
serial_port = '/dev/ttyUSB0'  #  listening port, type ls /dev/ttyUSB* in shell for available ports
ser = serial.Serial(serial_port, baud_rate)
count = 0


t_end = time.time() + 8
while time.time() < t_end:
    line = ser.readline();
    line = line.decode("utf-8")  #  ser.readline returns a binary, convert to string
    
    if line.startswith("PH"):
        ph = line.partition('=')[2]
        print(ph)
        intph = int(ph.replace(".",""))
        if intph <= 610:
            phalert = "true"
        elif intph >= 790:
            phalert = "true"
        else:
            phalert = "false"
        print("PHalert is: " + phalert)
    elif line.startswith("Temperature"):
        splittedline = line.partition('=')[2]
        temp = splittedline.partition(' PH=')[0]
        print(temp)
        temperature = temp.replace(".","")
        inttemp = int(temperature)
        if inttemp >= 2600:
            tempalert = "true"
        elif inttemp <= 2250:
            tempalert = "true"
        else:
            tempalert = "false"
        print("Tempalert is: " + tempalert)
    
    time.sleep(5)
    line = ser.readline();
    line = line.decode("utf-8")  #  ser.readline returns a binary, convert to string
    
    if line.startswith("PH"):
        ph = line.partition('=')
        print(ph)
    elif line.startswith("Temperature"):
        splittedline = line.partition('=')[2]
        temp = splittedline.partition(' PH=')[0]
        temperature = temp.replace(".","")
        inttemp = int(temperature)
        if inttemp >= 2600:
            tempalert = "true"
        elif inttemp <= 2250:
            tempalert = "true"
        else:
            tempalert = "false"
        print("Tempalert is: " + tempalert)
    
#JSON part
# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M")
data_set = [{
    "name": "Aquarium",
    " id": "Aquarium",
    "type": 1,
    "localIP": "192.168.178.24",
    "APName": "AquaNet",
    "APIP": "192.168.4.10",
    "temp": temperature,
    "tempAlert": tempalert,
    "minTemp": 2300,
    "maxTemp": 2600,
    "tempAdj": 50,
    "light": "PH: " + ph,
    "lightAlert": phalert,
    "minOnLight": 700,
    "maxOnLight": 1024,
    "lightOn": "08:00-15:00",
    "minOffLight": 0,
    "maxOffLight": 1024,
    "lightOff": "21:00-07:00",
    "waterLevelAlert": "false",
    "powerAlert": "false",
    "oneAlert": "true",
    "date": dt_string
}]


with open('/var/www/html/getData.json', 'w') as outfile:
    json.dump(data_set, outfile)
