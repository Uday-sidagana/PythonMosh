'''import os

# dir= os.getcwd()
# print(dir)
cont = os.listdir("/Users/macbookair/Desktop/python/Mosh/Harry")
print(cont)'''


#Speech Recognizition -> conversion into text using pocketSphinx -> text to speech via pyttsx3


"""import pyttsx3
import pocketsphinx

import speech_recognition as sr

listens = sr.Recognizer()
with sr.Microphone() as source:
    print("speak")
    text= listens.listen(source)
    print("spoke")
recognize = listens.recognize_sphinx(text)
engine = pyttsx3.init()
engine.say(recognize)

engine.runAndWait()"""

#