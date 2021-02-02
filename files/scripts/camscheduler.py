#!/usr/bin/python

import schedule
import time
import os

def FishVideo():
    os.system('python3 fishvideo.py')
    return

schedule.every(5).hours.do(FishVideo)


while True:
        schedule.run_pending()
        time.sleep(60)
