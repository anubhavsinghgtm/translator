import pandas as pd
import pyttsx3 as pt
import speech_recognition as sr
from googletrans import Translator
tr = Translator()

def output(text):
    engine = pt.init()
    engine.say(text)
    engine.runAndWait()


def converter(words):
    translated_words = tr.translate(words).text
    print("In English: ", translated_words)
    output(translated_words)
    return




def takeCommandHindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='hi-In')
            print("Your request is: '", query,"'")
            converter(query)
        except Exception as e:
            print(e)
            print('Say that again sir...')
            return "None"
        return
    
def HindiToEnglish():
    takeCommandHindi()