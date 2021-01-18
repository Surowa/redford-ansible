import os
import telegram
import time

bot = telegram.Bot(token="662345039:AAFzRlDxZLpKckfDDvxQVnvn-byYyl9j7pg")
chat_id=-297221617

#Remove old files 
os.system('sudo rm fishvideo.h264')
os.system('sudo rm fishvideo.mp4')
time.sleep(2)

#Turn on the light
os.system('sudo pilight-send -p kaku_switch -i 25544186 -u 0 -t')
time.sleep(4)

#Get the video
os.system('raspivid -t 10000 -w 640 -h 480 -fps 25 -b 20000000 -p 0,0,640,480 -vf -hf -o fishvideo.h264')
os.system('MP4Box -add fishvideo.h264 fishvideo.mp4')
time.sleep(2)

# Sends a message to the chat
bot.sendVideo(chat_id=chat_id, video=open('./fishvideo.mp4', 'rb'))

#Turn off the light
os.system('sudo pilight-send -p kaku_switch -i 25544186 -u 0 -f')
time.sleep(2)
