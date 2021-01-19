import sys
import os
import time
import subprocess
from playsound import playsound
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pandas as pd
import telegram
import RedfordCommands as redford

bot = telegram.Bot(token="662345039:AAFzRlDxZLpKckfDDvxQVnvn-byYyl9j7pg")
personalchat_id=669518538

try:
    startid = bot.get_updates()[-1].message.message_id

except:
    startid = '1'


if __name__ == '__main__':
    while True:
        time.sleep(3)
        updates = bot.get_updates()
        try:
            latestupdate = updates[-1]
            latestupdateid = latestupdate.message.message_id
            
            if latestupdateid !=  startid:
                print("Action executed for command: " + latestupdate.message.text)
                command = latestupdate.message.text
                os.system("python3 Redford.py \"" + command + "\" telegram")
                startid = latestupdateid
                
            else:
                time.sleep(1)
        except:
            time.sleep(1)
            
        
else:
    time.sleep(1)