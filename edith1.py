import speech_recognition as sr
import sys, time, os
import pyttsx3 as tts
import random

Baza_Pytan="Z:/Baza/BazaPytan.txt"
Baza_Odpowiedzi="Z:/Baza/BazaOdpowiedzi.txt"

engine=tts.init('sapi5')
engine.setProperty('voice',engine.getProperty('voices')[2].id)
engine.setProperty('rate',150)

r = sr.Recognizer()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def getText():
    with sr.Microphone() as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        text=r.recognize_google(audio,language="pl-PL")
        if text=="":
            return None
        else:
            return text

f=open(Baza_Pytan,encoding='utf8')
linie=f.readlines()
f1=open(Baza_Odpowiedzi,encoding='utf8')
linie10=f1.readlines()

Wykryj=linie[1].split(',')

def if_Exists(string,slowa):
    return [element for element in slowa if element in string.lower()]

while True:
    time.sleep(0.5)
    current=getText()
    print(current)
    if len(if_Exists(current,Wykryj)):
         print('słucham')
         speak('słucham')
         if len(if_Exists(current,Wykryj)):      
            if 'zakończ' in current:
                break
   

