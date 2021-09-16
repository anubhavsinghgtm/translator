from englisttohindi.englisttohindi import EngtoHindi
import speech_recognition as sr
import pyttsx3
from googletrans import Translator
r=sr.Recognizer()
translator = Translator()
while True:
    with sr.Microphone() as source:
        x="Let's start"
        res = EngtoHindi(x)
        print(x)
        result = translator.translate(x, dest='hi')
        print(result)
        print(res.convert)
        pyttsx3.speak(res.convert)
        audio=r.listen(source)
        print("converting")
    eng=r.recognize_google(audio)
    if (("close" in eng) or ("exit" in eng) or ("stop" in eng)) and ("app" in eng):
        c="closed"
        re = EngtoHindi(c)
        pyttsx3.speak(re.convert)
        result = translator.translate(c, dest='hi')
        print(result)
        break
    print("you spoke",eng)
    hin=EngtoHindi(eng)
    print("this is how it is spoken  in HIndi : ")
    result = translator.translate(eng, dest='hi')
    print(result)
    print(hin.convert)
    pyttsx3.speak(hin.convert)
    
