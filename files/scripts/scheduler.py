#!/usr/bin/python

import schedule
import time
import os
import datetime
from suntime import Sun, SunTimeException
timedelta = 1 #Number of hours beyond GMT, in summertime extra hour because of daylight saving
latitude = 50.89
longitude = 5.75
sun = Sun(latitude, longitude)
sunset = sun.get_sunset_time()
sunrise = sun.get_sunrise_time()
daylightsavingsunset = sunset + datetime.timedelta(hours=timedelta)
daylightsavingsunrise= sunrise + datetime.timedelta(hours=timedelta)
print("Sunrise: " + daylightsavingsunrise.strftime('%H:%M'))
print("Sunset: " + daylightsavingsunset.strftime('%H:%M'))

def FishVideo():
    os.system('python3 fishvideo.py')
    return
    
def LongFishVideo():
    os.system('python3 longfishvideo.py')
    return

def PompAan():
    os.system('sudo pilight-send -p kaku_switch -i 25544186 -u 2 -t')
    return

def PompUit():
    os.system('sudo pilight-send -p kaku_switch -i 25544186 -u 2 -f')
    return

def WaterkokerUit():
    os.system('sudo pilight-send -p kaku_switch -i 25544186 -u 1 -f')
    return

def WaterkokerAan():
    os.system('sudo pilight-send -p kaku_switch -i 25544186 -u 1 -t')
    return

def AqualichtAan():
    os.system('sudo pilight-send -p kaku_switch -i 25544186 -u 0 -t')
    return

def AquaLichtUit():
    os.system('sudo pilight-send -p kaku_switch -i 25544186 -u 0 -f')
    return

def GuineaPigVideo():
    os.system("python3 /home/pi/redford-ansible/files/scripts/guineapigvideo.py")
    return
    
def KerstboomUit():
    os.system("sudo sh /home/pi/redford-ansible/files/scripts/kerstboom_uit.sh")
    
def KerstboomAan():
    os.system("sudo sh /home/pi/redford-ansible/files/scripts/kerstboom_aan.sh")
    
darktime = daylightsavingsunset.strftime('%H:%M')
lighttime = daylightsavingsunrise.strftime('%H:%M')

schedule.every().day.at("08:00").do(PompAan)
schedule.every().day.at("15:00").do(AqualichtAan)
schedule.every(10).minutes.do(WaterkokerUit)
#schedule.every(120).minutes.do(GuineaPigVideo)
schedule.every().day.at("22:30").do(AquaLichtUit)
schedule.every().day.at("23:00").do(PompUit)


while True:
        schedule.run_pending()
        sunset = sun.get_sunset_time()
        daylightsavingsunrise= sunrise + datetime.timedelta(hours=timedelta)
        daylightsavingsunset = sunset + datetime.timedelta(hours=timedelta)
        time.sleep(60)
