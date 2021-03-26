#!/usr/bin/python

import schedule
import time
import os
import datetime
from suntime import Sun, SunTimeException
timedelta = 1 #Number of hours beyond GMT, in summertime extra hour because of daylight saving, then make it 2 temporarily
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
    os.system('sudo pilight-send -p kaku_switch -i 38045566 -u 2 -t')
    return

def AquaLichtUit():
    os.system('sudo pilight-send -p kaku_switch -i 38045566 -u 2 -f')
    return

def BuitenLichtAan():
    os.system('sudo pilight-send -p kaku_switch -i 38045566 -u 0 -t')
    return

def BuitenLichtUit():
    os.system('sudo pilight-send -p kaku_switch -i 38045566 -u 0 -f')
    return

def TvMeubelLampAan():
    os.system('sudo pilight-send -p kaku_switch -i 38045566 -u 1 -t')
    return

def TvMeubelLampUit():
    os.system('sudo pilight-send -p kaku_switch -i 38045566 -u 1 -f')
    return

def LampNaastBankAan():
    os.system('sudo pilight-send -p kaku_switch -i 25544186 -u 0 -t')
    return

def LampNaastBankUit():
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
schedule.every().day.at("15:30").do(AqualichtAan)
schedule.every().day.at(darktime).do(LampNaastBankAan)
schedule.every().day.at(darktime).do(TvMeubelLampAan)
schedule.every().day.at(darktime).do(BuitenLichtAan)

schedule.every().day.at("21:30").do(AquaLichtUit)
schedule.every().day.at("23:15").do(LampNaastBankUit)
schedule.every().day.at("23:30").do(TvMeubelLampUit)
schedule.every().day.at("23:30").do(BuitenLichtUit)
schedule.every().day.at("00:30").do(BuitenLichtUit)
schedule.every().day.at("01:00").do(PompUit)

schedule.every(10).minutes.do(WaterkokerUit)
#schedule.every(120).minutes.do(GuineaPigVideo)

while True:
        schedule.run_pending()
        sunset = sun.get_sunset_time()
        sunrise = sun.get_sunrise_time()
        daylightsavingsunrise= sunrise + datetime.timedelta(hours=timedelta)
        daylightsavingsunset = sunset + datetime.timedelta(hours=timedelta)
        time.sleep(60)
