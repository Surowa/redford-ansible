import os
import telegram
import time

bot = telegram.Bot(token="662345039:AAFzRlDxZLpKckfDDvxQVnvn-byYyl9j7pg")
chat_id=-297221617

#Remove old files 
os.system('sudo rm fishvideo.h264')
os.system('sudo rm fishvideo.mp4')
time.sleep(2)


#Get the video
os.system('raspivid -t 10000 -w 640 -h 480 -fps 25 -b 1200000 -p 0,0,640,480 -vf -hf -o fishvideo.h264')
os.system('MP4Box -add fishvideo.h264 fishvideo.mp4')
time.sleep(2)

# Sends a message to the chat
bot.sendVideo(chat_id=chat_id, video=open('./fishvideo.mp4', 'rb'))

