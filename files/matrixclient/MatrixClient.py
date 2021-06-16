import os
import pyaudio
import wave
import requests
import json
from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()

# recording configs
CHUNK = 2048
FORMAT = pyaudio.paInt16
CHANNELS = 8
RATE = 96000
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME = "stream.wav"

# create & configure microphone
mic = pyaudio.PyAudio()
stream = mic.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
                input_device_index=1)

print("* recording")

# read & store microphone data per frame read
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

# kill the mic and recording
stream.stop_stream()
stream.close()
mic.terminate()

# combine & store all microphone data to output.wav file
outputFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
outputFile.setnchannels(CHANNELS)
outputFile.setsampwidth(mic.get_sample_size(FORMAT))
outputFile.setframerate(RATE)
outputFile.writeframes(b''.join(frames))
outputFile.close()

#Send data to speech recognizer
understood_text = os.popen('curl -T /home/pi/shared/stream.wav "http://redfordbrain.local:8888/client/dynamic/recognize"').read()
print(understood_text)
json_text = json.loads(str(understood_text))
print(json_text)
utterance = json_text['hypotheses'][0]['utterance']
print(utterance)
utterance_tokenenized = tokenizer.tokenize(utterance)

#Sent recognized text to AI to do something with it
url = f"http://redfordbrain.local:5000/api/v1/speech?command='{utterance_tokenenized}'"
command = f"curl --request GET --url {url}"
response = os.popen(command).read()
print(response)
