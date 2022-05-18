import azure.cognitiveservices.speech as speechsdk
import sys
from playsound import playsound
import lxml.etree
import lxml.builder
import random
import subprocess
import time
import telegram
from lxml import etree as ET
from collections import OrderedDict
import datetime
import os


def GoedeMorgen(command):
    speech_key, service_region, language = "854386192c9a40ebbb3bfc623744407f", "eastus", "nl-NL"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region, speech_recognition_language=language)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)
    possibletexts = [
        "Goedemorgen, ook leuk om jou te zien.",
        "Een hele goede morgen",
        "Schitterend als altijd, deze dag.",
        "Goedemorgen, begin de dag met een lach.",
        "Hey! Dit belooft een leuke dag te worden."
    ]
    text = random.choice(possibletexts)


    #Puts it in XML
    root = ET.Element('speak', version=u"1.0", xmlns=u"https://www.w3.org/2001/10/synthesis")
    root.set("{http://www.w3.org/XML/1998/namespace}lang", "en-US")
    voice = ET.SubElement(root, 'voice', name=u"nl-NL-HannaRUS")
    voice.text = text
    tree = ET.ElementTree(root)
    tree.write('ssml.xml', pretty_print=True, xml_declaration=True,   encoding="utf-8")
        
    # Synthesizes the received text to speech.
    result = synthesizer.speak_text_async(text).get()
    ssml_string = open("ssml.xml", "r").read()
    result = synthesizer.speak_ssml_async(ssml_string).get()
    stream = speechsdk.AudioDataStream(result)
    stream.save_to_wav_file("stream.wav")
    playsound('stream.wav')
    return text

def SpreekTekst(spreektekst):
    speech_key, service_region, language = "854386192c9a40ebbb3bfc623744407f", "eastus", "nl-NL"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region, speech_recognition_language=language)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)
    text = spreektekst

    #Puts it in XML
    root = ET.Element('speak', version=u"1.0", xmlns=u"https://www.w3.org/2001/10/synthesis")
    root.set("{http://www.w3.org/XML/1998/namespace}lang", "en-US")
    voice = ET.SubElement(root, 'voice', name=u"nl-NL-HannaRUS")
    voice.text = text
    tree = ET.ElementTree(root)
    tree.write('ssml.xml', pretty_print=True, xml_declaration=True,   encoding="utf-8")
        
    # Synthesizes the received text to speech.
    result = synthesizer.speak_text_async(text).get()
    ssml_string = open("ssml.xml", "r").read()
    result = synthesizer.speak_ssml_async(ssml_string).get()
    stream = speechsdk.AudioDataStream(result)
    stream.save_to_wav_file("stream.wav")
    playsound('stream.wav')

def SpreekTekstNoors(spreektekst):
    speech_key, service_region, language = "854386192c9a40ebbb3bfc623744407f", "eastus", "no-NO"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region, speech_recognition_language=language)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)
    text = spreektekst

    #Puts it in XML
    root = ET.Element('speak', version=u"1.0", xmlns=u"https://www.w3.org/2001/10/synthesis")
    root.set("{http://www.w3.org/XML/1998/namespace}lang", "en-US")
    voice = ET.SubElement(root, 'voice', name=u"nb-NO-HuldaRUS")
    voice.text = text
    tree = ET.ElementTree(root)
    tree.write('ssml.xml', pretty_print=True, xml_declaration=True,   encoding="utf-8")
        
    # Synthesizes the received text to speech.
    result = synthesizer.speak_text_async(text).get()
    ssml_string = open("ssml.xml", "r").read()
    result = synthesizer.speak_ssml_async(ssml_string).get()
    stream = speechsdk.AudioDataStream(result)
    stream.save_to_wav_file("stream.wav")
    playsound('stream.wav')

def TotZiens():
    speech_key, service_region, language = "854386192c9a40ebbb3bfc623744407f", "eastus", "nl-NL"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region, speech_recognition_language=language)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)
    possibletexts = [
        "Tot ziens, hopelijk zie ik je snel weer!",
        "Tot de volgende keer",
        "Ik zal aan je denken, voor zover robots dat kunnen.",
        "Ik spreek je snel weer.",
        "Tot weerziens."
    ]
    text = random.choice(possibletexts)

    #Puts it in XML
    root = ET.Element('speak', version=u"1.0", xmlns=u"https://www.w3.org/2001/10/synthesis")
    root.set("{http://www.w3.org/XML/1998/namespace}lang", "en-US")
    voice = ET.SubElement(root, 'voice', name=u"nl-NL-HannaRUS")
    voice.text = text
    tree = ET.ElementTree(root)
    tree.write('ssml.xml', pretty_print=True, xml_declaration=True,   encoding="utf-8")
        
    # Synthesizes the received text to speech.
    result = synthesizer.speak_text_async(text).get()
    ssml_string = open("ssml.xml", "r").read()
    result = synthesizer.speak_ssml_async(ssml_string).get()
    stream = speechsdk.AudioDataStream(result)
    stream.save_to_wav_file("stream.wav")
    playsound('stream.wav')

def VerklaarWeerVanVandaag(weersamenvatting):
    speech_key, service_region, language = "854386192c9a40ebbb3bfc623744407f", "eastus", "nl-NL"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region, speech_recognition_language=language)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)
    text = weersamenvatting

    #Puts it in XML
    root = ET.Element('speak', version=u"1.0", xmlns=u"https://www.w3.org/2001/10/synthesis")
    root.set("{http://www.w3.org/XML/1998/namespace}lang", "en-US")
    voice = ET.SubElement(root, 'voice', name=u"nl-NL-HannaRUS")
    voice.text = text
    tree = ET.ElementTree(root)
    tree.write('ssml.xml', pretty_print=True, xml_declaration=False, encoding="utf-8")

    # Synthesizes the received text to speech.
    result = synthesizer.speak_text_async(text).get()
    ssml_string = open("ssml.xml", "r").read()
    result = synthesizer.speak_ssml_async(ssml_string).get()
    stream = speechsdk.AudioDataStream(result)
    stream.save_to_wav_file("stream.wav")
    playsound('stream.wav')

def VertelGrap():
    speech_key, service_region, language = "854386192c9a40ebbb3bfc623744407f", "eastus", "nl-NL"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region, speech_recognition_language=language)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)
    possibletexts = [
        "Er zit een meisje op straat te huilen. Er komt een man komt voorbij die bezorgd vraagt: ‘Wat is er aan de hand?’‘Ik ben mijn euro kwijtgeraakt,’ snikt het meisje.‘Ach kind, wat naar,’ antwoordt de man. ‘Hier heb je er eentje van mij.’ Het meisje gaat nog harder huilen.‘Waarom huil je nu?’ vraagt de man verbaasd. Het meisje zegt: ‘Ik had beter kunnen zeggen dat ik vijf euro kwijt was!’",
        "Er zit een man in de stad. Hij schildert een huis. Iris komt voorbij en zegt tegen haar moeder: ‘Erg hè? Die man is vast te arm om een fototoestel te kopen…’"
    ]
    text = random.choice(possibletexts)

    #Puts it in XML
    root = ET.Element('speak', version=u"1.0", xmlns=u"https://www.w3.org/2001/10/synthesis")
    root.set("{http://www.w3.org/XML/1998/namespace}lang", "en-US")
    voice = ET.SubElement(root, 'voice', name=u"nl-NL-HannaRUS")
    voice.text = text
    tree = ET.ElementTree(root)
    tree.write('ssml.xml', pretty_print=True, xml_declaration=True,   encoding="utf-8")
        
    # Synthesizes the received text to speech.
    result = synthesizer.speak_text_async(text).get()
    ssml_string = open("ssml.xml", "r").read()
    result = synthesizer.speak_ssml_async(ssml_string).get()
    stream = speechsdk.AudioDataStream(result)
    stream.save_to_wav_file("stream.wav")
    playsound('stream.wav')
    return text

def DigitaleUitkijkpost():
    bot = telegram.Bot(token="662345039:AAFzRlDxZLpKckfDDvxQVnvn-byYyl9j7pg")
    chat_id=669518538

    if __name__ == '__main__':
        while True:
            time.sleep(5)
            p = subprocess.Popen("sudo arp-scan -l | grep 64:a2:f9:2f:26:80", stdout=subprocess.PIPE, shell=True)
            (output, err) = p.communicate()
            p_status = p.wait()
            if output:
                bot.sendMessage(chat_id=chat_id, text="Redford heeft iemand gespot..")
                raise SystemExit
            else:
                time.sleep(1)

def VertaalTekst(tekst):
    import os, requests, uuid, json
    bot = telegram.Bot(token="662345039:AAFzRlDxZLpKckfDDvxQVnvn-byYyl9j7pg")
    personalchat_id=669518538
    #key_var_name = '849a6a2480e348d990b9e16947b474d0'
    #if not key_var_name in os.environ:
    #    raise Exception('Please set/export the environment variable: {}'.format(key_var_name))
    #subscription_key = '3be8291235e5446f837516b356917ce6'

    #endpoint_var_name = 'https://redfordtranslate.cognitiveservices.azure.com/'
    #if not endpoint_var_name in os.environ:
    #    raise Exception('Please set/export the environment variable: {}'.format(endpoint_var_name))
    endpoint = "https://api-eur.cognitive.microsofttranslator.com"

    # If you encounter any issues with the base_url or path, make sure
    # that you are using the latest endpoint: https://docs.microsoft.com/azure/cognitive-services/translator/reference/v3-0-translate
    path = '/translate?api-version=3.0'
    params = '&to=no&to=nl'
    constructed_url = endpoint + path + params

    headers = {
        'Ocp-Apim-Subscription-Key': '3be8291235e5446f837516b356917ce6',
        'Ocp-Apim-Subscription-Region' : 'westeurope',
        'Content-type' : 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text' : tekst
    }]
    request = requests.post(constructed_url, headers=headers, json=body)
    response = request.json()
    #Naar Noors 
    noorsetekst = response[0]['translations'][0]['text']
    bot.send_message(chat_id=personalchat_id, text=noorsetekst)
    return noorsetekst
    #NL  = print(response[0]['translations'][1]['text'])
    #print(json.dumps(response, sort_keys=True, indent=4, separators=(',', ': ')))

def TelegramStuurBericht(bericht):
    bot = telegram.Bot(token="662345039:AAFzRlDxZLpKckfDDvxQVnvn-byYyl9j7pg")
    personalchat_id=669518538
    bot.send_message(chat_id=personalchat_id, text=bericht)

def NoteerNotitie(notitietitel, notitie):
    import sqlite3
    conn = sqlite3.connect('todolistsdb.db')
    cur = conn.cursor()
    query = "INSERT INTO tb_notities (title, content) VALUES (?, ?)"
    val = (notitietitel, notitie)
    cur.execute(query, val)
    conn.commit()
    conn.close()

def HaalNotitieOp(notitietitel):
    import sqlite3
    conn = sqlite3.connect('todolistsdb.db')
    cur = conn.cursor()
    query = "SELECT content FROM tb_notities WHERE title LIKE ?"
    val = (notitietitel,)
    try:
        cur.execute(query, val)
        notesraw = cur.fetchall()
        for note in notesraw:
            notitie = note[0]
            print(notitie)
    except:
        notitie = "Notitie kon niet worden gevonden onder die naam. Probeer eens om alle notities weer te geven met <Notitie alles> geven."
    conn.commit()
    conn.close()
    return notitie

def NotitiePlus(aanvulling,notitietitel):
    import sqlite3
    conn = sqlite3.connect('todolistsdb.db')
    cur = conn.cursor()
    try:
        query = "SELECT content FROM tb_notities WHERE title LIKE ?"
        val = (notitietitel,)
        cur.execute(query, val)
        notesraw = cur.fetchall()
        for note in notesraw:
                notitie = note[0]
                print(notitie)
                updatequery = "UPDATE tb_notities SET content = ?  WHERE title LIKE ?"
                val = (aanvulling,notitie)
                cur.execute(updatequery, val)
                notesraw = cur.fetchall()
    except:
        notitie = "Notitie kon niet worden gevonden onder die naam. Probeer eens om alle notities weer te geven met <Notitie alles> geven."
    conn.commit()
    conn.close()
    return notitie

def HaalAlleNotitiesOp():
    import sqlite3
    conn = sqlite3.connect('todolistsdb.db')
    cur = conn.cursor()
    query = "SELECT title FROM tb_notities"
    count = 0
    try:
        cur.execute(query)
        notesraw = cur.fetchall()
        for note in notesraw:
            notities = note[0]
            count = count + 1
        return notesraw
    except:
        notities = "Geen notities beschikbaar of database niet bereikbaar."
        return notities
    conn.commit()
    conn.close()
    

def VerwijderNotitie(notitietitel):
    import sqlite3
    conn = sqlite3.connect('todolistsdb.db')
    cur = conn.cursor()
    val = (notitietitel,)
    query = "DELETE FROM tb_notities WHERE title LIKE ?"
    cur.execute(query,val)
    conn.commit()
    conn.close()

def HaalWolkendichtheidOpText():
    import requests
    import json
    from requests.auth import HTTPBasicAuth
    sleutel = "E5HdOxTItp_UluSu4n8x3RFfBBWHb7Zn"
    solcast_uri = "https://api.solcast.com.au/world_radiation/estimated_actuals?latitude=50.921978&longitude=5.749388&hours=168"
    headers = {'accept': 'application/json'}
    request = requests.get(solcast_uri, auth=HTTPBasicAuth(sleutel, ''), headers=headers)
    response = request.json()
    cloudiness = response['estimated_actuals'][0]['cloud_opacity']
    if cloudiness >= 70:
        result = "Cloudy weather"
    elif 31 <= cloudiness <= 69:
        result = "Partly cloudy currently"
    else:
        result = "Clear weather"
    return result

def HaalWolkendichtheidOpPercentage():
    import requests
    import json
    from requests.auth import HTTPBasicAuth
    sleutel = "E5HdOxTItp_UluSu4n8x3RFfBBWHb7Zn"
    solcast_uri = "https://api.solcast.com.au/world_radiation/estimated_actuals?latitude=50.921978&longitude=5.749388&hours=168"
    headers = {'accept': 'application/json'}
    request = requests.get(solcast_uri, auth=HTTPBasicAuth(sleutel, ''), headers=headers)
    response = request.json()
    cloudiness = response['estimated_actuals'][0]['cloud_opacity']
    return cloudiness

def VoerVissen():
    # https://reefbuilders.com/2013/08/31/neptune-afs-automatic-feeding-system-hobbys-controllable-fish-feeder/
    return