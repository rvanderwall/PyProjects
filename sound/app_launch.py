import os
import speech_recognition as sr
import subprocess

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""
# https://towardsdatascience.com/building-a-simple-voice-assistant-for-your-mac-in-python-62247543b626
#!brew install portaudio
#!brew install elasticsearch
#
#!pip install SpeechRecognition
#!pip install pyaudio
#!pip install elasticsearch
#!pip install selenium
"""

APP_DIR="/Applications"
ACTIVATION_PHRASES=["hey mac","amac"]
VOICE='fred'

#
#   SPEAKING AND LISTENING
#
def get_speech(prompt):
    print(prompt)
    print("Start acquiring speech")
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Determining ambient noise")
        r.adjust_for_ambient_noise(source)
        print("Start talking")
        audio = r.listen(source)
        print("Captured speech")
        transcript = r.recognize_google(audio)
        print("You said:" + transcript)
        return transcript.lower()


def say(text):
    subprocess.call(["say",f"-v{VOICE}", text])
    print("Done speaking: " + text)


def activate():
   spoken = get_speech("Say " + ACTIVATION_PHRASES[0] + " to activate")
   print(f"See if {spoken} is in {ACTIVATION_PHRASES}")
   if spoken in ACTIVATION_PHRASES:
       print("Activated")
       return True
   else:
       return False


#
#  MAC OS specific
#
def generate_app_command(app):
    app = app.replace(' ', '\ ')
    command = f"open {APP_DIR}/{app}.app"
    return command

def generate_app_commands():
    records = []
    apps = list(map(lambda x: x.split('.app')[0], os.listdir(APP_DIR)))
    for app in apps:
        record = {}
        record['voice_command'] = f"open {app}"
        record['sys_command'] = generate_app_command(app)
        records.append(record)

    return records

def start_one_app(app):
    if ".app" in app:
        os.system(app)
    else:
        os.system(generate_app_command(app))


#
# Elastic Search
#
def save_app_commands(commands):
    es = Elasticsearch(['localhost:9200'])
    bulk(es, commands, index='voice_assistant',
        doc_type='text', raise_on_error=True)

def search_es(query):
    es = Elasticsearch(['localhost:9200'])
    res = es.search(index='voice_assistant', doc_type='text',
    body={
        "query":  {
            "match": {
                "voice_command": {
                    "query": query,
                    "fuzziness": 2
                }
            }
        }
    })
    return res['hits']['hits'][0]['_source']['sys_command']


#
# Selenium
#
def search_google(query):
    print("Search google for " + query)
    browser = webdriver.Chrome()
    browser.get('http://www.google.com')
    search = browser.find_element_by_name('q')
    search.send_keys(query)
    search.send_keys(Keys.RETURN)


#commands = generate_app_commands()
#save_app_commands(commands)
#print(search_es('open slack'))

while False:
    if activate():
        try:
            say("Hey Rob, how can I help you today?")
            cmd = get_speech("Say search or open")
            print("Got command " + cmd)
            if cmd == "stop":
                break

            if "search" in cmd:
                print("Searching with command " + cmd)
                search_google(cmd)
            else:
                print("Opening with command " + cmd)
                sys_command = search_es(cmd)
                start_one_app(sys_command)
        except:
            pass
    else:
        pass

search_google("how to build a voice assistant")
