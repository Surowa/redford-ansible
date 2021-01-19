import azure.cognitiveservices.speech as speechsdk
import sys
import os
import time
import subprocess
from playsound import playsound
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import telegram
import RedfordCommands as redford
import RedfordNLP as redfordnlp
import numpy as np
from keras.models import load_model
model = load_model('chatbot_model.h5')
import json
import random
import pickle
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))


command = sys.argv[1] #Get first argument command. 
input = command
hold = redfordnlp.RemoveStopWords(input)
entrymethod = sys.argv[2]

"""




else:
    seriekijktriggers = ["series", "serie", "aflevering"]
    if any(triggers in command for triggers in seriekijktriggers):
        #os.system('ssh@192.168.178.70 "sudo pilight-send -p kaku_switch -i 25544186 -u 1 -t"')
        bericht = "Stuur de serie in kwestie via een bericht op WhatsApp."
        if entrymethod == 'telegram':
            redford.TelegramStuurBericht(bericht)
        else:
            redford.SpreekTekst(bericht)

    graptriggers = ["Grap", "grap", "mop", "moppen", "grappen"]
    if any(triggers in command for triggers in graptriggers):
        if entrymethod == 'telegram':
            text = redford.VertelGrap()
            redford.TelegramStuurBericht(text)
        else:
            redford.VertelGrap()
    
    remindertriggers = ["Herinnering", "herinnering", "onthouden"]
    if any(triggers in command for triggers in remindertriggers):
        tekst = command.split(' ', 3)[3]
        redford.NoteerNotitie(tekst, tekst)
        bericht = 'Notitielijst ' + command + ' is aangemaakt.'
        if entrymethod == 'telegram':
            redford.TelegramStuurBericht(bericht)
        else:
            redford.SpreekTekst(bericht)
    
    notitieaanmaaktriggers = ["notitie", "Notitie", "kladblok",  "opschrijven"]
    if any(triggers in command for triggers in notitieaanmaaktriggers):
        notitieophaaltriggers = ["ophalen", "inzien", "lezen"]
        notitietiteltriggers = ["geef alles", "alles", "allemaal"]
        notitieverwijdertriggers = ["verwijderen", "weghalen"]
        notitieaanpastriggers = ["+", "plus"]
        if any(triggers in command for triggers in notitieophaaltriggers):
            notitietitel = command.split(' ', 3)[2]
            notitie = redford.HaalNotitieOp(notitietitel)
            redford.TelegramStuurBericht(notitie)
        elif any(triggers in command for triggers in notitietiteltriggers):
            notities = redford.HaalAlleNotitiesOp()
            redford.TelegramStuurBericht(notities)
        elif any(triggers in command for triggers in notitieaanpastriggers):
            notitietitel = command.split(' ', 3)[2]
            aanvulling = command.split(' ', 3)[3]
            notities = redford.NotitiePlus(aanvulling, notitietitel)
            redford.TelegramStuurBericht(notities)
        elif any(triggers in command for triggers in notitieverwijdertriggers):
            notitietitel = command.split(' ', 3)[2]
            redford.VerwijderNotitie(notitietitel)
            redford.TelegramStuurBericht("Notitie is verwijderd")
        else:
            tekst = command.split(' ', 3)[3]
            notitietitel = command.split(' ', 3)[2]
            redford.NoteerNotitie(notitietitel, tekst)
            bericht = 'Notitie ' + notitietitel + ' is aangemaakt.'
            redford.TelegramStuurBericht(bericht)

    
    
    vertaaltriggers = ["vertaal", "Vertaal", "vertalen", "geef vertaling", "Geef Noorse vertaling", "vertaling geven", "Vertaling geven"]
    if any(triggers in command for triggers in vertaaltriggers):
        tekst = command.split(' ', 3)[3]
        antwoord = redford.VertaalTekst(tekst)
        print(antwoord)
        redford.SpreekTekstNoors(antwoord)

    helptriggers = ["help", "commando's", "commando", "hulp", "commandos", "Hulp", "Help", "Commando's", "Commando"]
    if any(triggers in command for triggers in helptriggers):
        tekst ="Beschikbare commando's zijn: -weer (update over het weer); -corona (laatste nieuws over het virus); -maak notitie <notitienaam> <notitie> (notitie aanmaken), notitie ophalen <notitienaam>, notitie alles, notitie verwijderen <notitienaam>, -vertaal naar Noors <zin>. Notitienaam mag maar 1 woord zijn."
        if entrymethod == 'telegram':
            redford.TelegramStuurBericht(tekst)
        else:
            redford.SpreekTekst(tekst)
"""

#NEW

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res

#cleaned_up_command = clean_up_sentence(command)
#bow_command = bow(cleaned_up_command, words, show_details=True)

result = chatbot_response(command)
if "AQUARIUM_AAN" in result:
    if entrymethod == 'telegram':
        text = redford.GoedeMorgen(command)
        redford.TelegramStuurBericht(text)
        
    else:
        redford.GoedeMorgen(command)

elif "WEER_RESPONSE" in result:
    URL = "https://weerslag.nl/service/weersverwachtingnederland/"
    page = requests.get(URL.strip())
    soup = BeautifulSoup(page.content, 'html.parser');
    job_elems = soup.find_all('p', class_='hyperBlack')
    weersamenvatting = job_elems[2].find('a').get_text()
    if entrymethod == 'telegram':
        redford.TelegramStuurBericht(weersamenvatting)
    else:
        redford.VerklaarWeerVanVandaag(weersamenvatting)
elif "CORONA_RESPONSE" in result:
    URL = "https://www.rivm.nl/coronavirus-covid-19/actueel"
    page = requests.get(URL.strip())
    soup = BeautifulSoup(page.content, 'html.parser')
    job_elems = soup.find_all('div', class_='container container-spacer-sm content nobg clearfix')
    coronasamenvatting = job_elems[0].get_text()
    redford.TelegramStuurBericht(coronasamenvatting)
    
elif "LAMP_AAN_RESPONSE" in result:
    os.system('ssh pi@192.168.178.70 "sudo pilight-send -p kaku_switch -i 25544186 -u 0 -t"')
    bericht = "Lamp van het aquarium is aangezet."
    if entrymethod == 'telegram':
        redford.TelegramStuurBericht(bericht)
    else:
        redford.SpreekTekst(bericht)
elif "LAMP_UIT_RESPONSE" in result:
    os.system('ssh pi@192.168.178.70 "sudo pilight-send -p kaku_switch -i 25544186 -u 0 -f"')
    bericht = "Lamp van het aquarium is uitgezet."
    if entrymethod == 'telegram':
        redford.TelegramStuurBericht(bericht)
    else:
        redford.SpreekTekst(bericht)
elif "POMP_AAN_RESPONSE" in result:
    os.system('ssh pi@192.168.178.70 "sudo pilight-send -p kaku_switch -i 25544186 -u 2 -t"')
    bericht = "De pomp is aangezet."
    if entrymethod == 'telegram':
        redford.TelegramStuurBericht(bericht)
    else:
        redford.SpreekTekst(bericht)

elif "POMP_UIT_RESPONSE" in result:
    os.system('ssh pi@192.168.178.70 "sudo pilight-send -p kaku_switch -i 25544186 -u 2 -f"')
    bericht = "De pomp is uitgezet."
    if entrymethod == 'telegram':
        redford.TelegramStuurBericht(bericht)
    else:
        redford.SpreekTekst(bericht)
else:
    redford.TelegramStuurBericht(result)
