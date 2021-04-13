
# https://towardsdatascience.com/building-a-simple-voice-assistant-for-your-mac-in-python-62247543b626
#!brew install portaudio
#!brew install elasticsearch
#
#!sudo xcodebuild -license accept
#!xcode-select --install
#!xcode-select --reset
#
#!pip install SpeechRecognition
#!pip install pyaudio
#!pip install elasticsearch


import speech_recognition as sr
import subprocess

def get_speech():
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

    return transcript


def say(text):
    subprocess.call(['say', text])


txt = get_speech()
say('yo dawg, whatup ' + txt)

