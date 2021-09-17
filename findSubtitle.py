import time
import pandas as pd
import pyttsx3 as pt
import speech_recognition as sr
from googletrans import Translator
import moviepy.editor as mp
tr = Translator()


# this function converts hindi into english
def converter(words):
    print('Translating text from hindi to english')
    translated_words = tr.translate(words).text
    print("In English: ", translated_words)
    output(translated_words)
    print('Saving the subtitles...')
    file = open('subtitle.txt', 'w')
    file.write(translated_words)
    file.close()
    print('Done')
    return



def output(text):
    engine = pt.init()
    
    # to set the rate of speaking
    engine.setProperty('rate',100)
    
    # to get the voices
    voices = engine.getProperty('voices')
    
     #female voice
    engine.setProperty('voice', voices[1].id)
    
    # to speak the text
    engine.say(text)
    
    # save the file in mp3 format
    engine.save_to_file(text, 'test.mp3') 
    
    engine.runAndWait()



def startConvertion(path = 'my_result.wav',lang = 'hi-IN'):
    with sr.AudioFile(path) as source:
        print('Fetching Audio File...')
        r = sr.Recognizer()
        audio_text = r.listen(source)
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
        
            # using google speech recognition
            print('Converting audio transcripts into text ...')
            text = r.recognize_google(audio_text)
            print(text)

            # to convert the hindi text to english
            converter(text)
    
        except:
            print('Sorry.. run again...')
            query = input("Type 'yes' to start again")
            if query == yes:
                subtitle()



def subtitle():
    # to take the file-name of video(only-name)
    video = input()

    try:
        # to get that video file from the storage
        print('Searching for the Video...')
        time.sleep(1)
        my_clip = mp.VideoFileClip(fr"{video}.mp4")

        # to retrieve the audio file from that video
        my_clip.audio.write_audiofile(r"my_result.wav")
        startConvertion()

    except OSError:
        print("Please try again file not found")
        query = input("Type 'yes' to continue")
        if query == 'yes':
            subtitle()



subtitle()
