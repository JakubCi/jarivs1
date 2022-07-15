import speech_recognition as sr
import pyttsx3 as tts
import sys, time, os
import webbrowser as w
from selenium import webdriver
import pyautogui as py
from random import randint
import random
import datetime
import requests
import json
import math
#Silnik recognizera
r=sr.Recognizer()
engine=tts.init('sapi5')
engine.setProperty('voice',engine.getProperty('voices')[2].id)
engine.setProperty('rate',150)
#Aktualny czas i data
data = time.strftime("%Y-%m-%d %H:%M", time.localtime()) 
godzina = time.strftime("%H:%M", time.localtime()) 
#Bazy danych
Notatnik="Z:/Baza/Notatnik.txt"
Baza_Pytan="Z:/Baza/BazaPytan.txt"
Baza_Odpowiedzi="Z:/Baza/BazaOdpowiedzi.txt"
piosenkibaza="Z:/Baza/piosenki.txt"
#globalne
czypytal=True
#pliki
chrome='C:/Program Files/Google/Chrome/Application/chrome.exe %s'
visualstudiocode='Z:/Microsoft VS Code/code.exe %s'
driver=webdriver.Chrome('Z:/PATH/chromedriver.exe')
#linki
yt='https://www.youtube.com/results?search_query='
google='https://www.google.com/search?q='
librus='https://portal.librus.pl/rodzina/synergia/loguj'
#funkcja speak do mowienia bota
def speak(text):
    engine.say(text)
    engine.runAndWait()
#funkcja gettext do zamiany mowy na tekst i nasluchiwania
def getText():
    try:
        with sr.Microphone() as source:
            print("Słucham...",end='\r')
            audio=r.listen(source)
            text=r.recognize_google(audio,language="pl-PL")
            
            if text=="":
                return None
            else:
                return text
    except:
        return None

##otwieranie bazy pytan i odpowiedzi oraz dodawanie linii do tablicy
f=open(Baza_Pytan,encoding='utf8')
linie=f.readlines()
f10=open(Baza_Odpowiedzi,encoding='utf8')
linie10=f10.readlines()
f20=open(piosenkibaza)
linie20=f20.readlines()
#if exist- czy baza zawiera frazy
def findByXpath(xpath):
    global driver
    elementy=driver.find_elements_by_xpath(xpath)
    while len(elementy)==0:
        time.sleep(0.5)
        elementy=driver.find_elements_by_xpath(xpath)
    return elementy[0]

def if_Exists(string,slowa):
    return [element for element in slowa if element in string.lower()]
#pytania
Wykryj=linie[1].split(',')
Dowidzenia=linie[3].split(',')
Zapisz=linie[5].split(',')
Usun=linie[7].split(',')
Odczytywanie_ostatniej=linie[9].split(',')
youtube=linie[11].split(',')
godzina1=linie[13].split(',')
informacje_o_bocie=linie[15].split(',')
imie_bota=linie[17].split(',')
pogoda=linie[19].split(',')
mozliwosci=linie[21].split(',')
dzieki=linie[23].split(',')
dzien=linie[25].split(',')
vsc=linie[27].split(',')
zglosnienie=linie[29].split(',')
sciszenie=linie[31].split(',')
budzenie_jarvisa=linie[33].split(',')
dobresamopoczucie=linie[35].split(',')
zlesamopoczucie=linie[37].split(',')
wchodzenienalibrusa=linie[39].split(',')
odpniewiem=linie[41].split(',')
odpowiedzitak=linie[43].split(',')
odpowiedzinie=linie[45].split(',')
imiebota=linie[47].split(',')
piosenkilosowe=linie[49].split(',')
przegladarka=linie[51].split(',')
#odpowiedzi
vscOdp=linie10[3].split(',')
powitania=linie10[5].split(',')
powitania2=linie10[7].split(',')
pytanie_o_dzien=linie10[9].split(',')
dobresamopoczucieODP=linie10[11].split(',')
zlesamopoczucieODP=linie10[13].split(',')
plany=linie10[15].split(',')
odpowiedziproste=linie10[17].split(',')
odpowiedzidoniewiem=linie10[19].split(',')
jakieplany=linie10[21].split(',')
#piosenki
p=linie20[0].split(',')

dt = datetime.datetime.now()

while True:
    time.sleep(0.5)
    aktualna=getText()
    print(""*50,end="\r")
    if aktualna!=None:
        print(aktualna)
        # dzisiejszydzien=dt.now()
        # if dt.now()!=dzisiejszydzien:
        #     czypytal=False
        #     print("czypytal false")
        # elif dt.now()==dzisiejszydzien:
        #     czypytal=True
        #     print("czypytal true")
        # if len(if_Exists(aktualna,Wykryj)) and czypytal==False:
        #     print("chuj")
        #     czypytal=True
        #     losowa=random.choice(pytanie_o_dzien)
        #     speak(losowa)
        #     pytanieodzien=getText()
        #     if len(if_Exists(pytanieodzien,dobresamopoczucie)):
        #         losowa=random.choice(dobresamopoczucieODP)
        #         speak(losowa)
        #         losowa2=random.choice(plany)
        #         speak(losowa2)
        #         plans=getText()
        #         if len(if_Exists(plans,odpniewiem)):
        #             losowa3=random.choice(odpowiedzidoniewiem)
        #             losowa4=random.choice(odpowiedziproste)
        #             speak(losowa3)
        #             plans2=getText()
        #             if len(if_Exists(plans2,odpowiedzitak)):
        #                 losowa5=random.choice(jakieplany)
        #                 speak(losowa5)
        #                 plans3=getText()
        #                 while len(if_Exists(plans3,odpowiedzinie)):
        #                     losowa10=random.choice(jakieplany)
        #                     speak(losowa10)
        #                     plans3=getText()
        #                     if len(if_Exists(plans3,odpowiedzitak)):
        #                         if 'dalsze' in losowa5:
        #                             speak("otwieram visual studio")
        #                     elif len(if_Exists(plans3,odpowiedzinie)):
        #                         speak("no to..")
        #             elif len(if_Exists(plans2,odpowiedzinie)):
        #                 speak(losowa4)
        #         else:
        #             curr=plans
        #     elif len(if_Exists(pytanieodzien,zlesamopoczucie)):
        #         losowa=random.choice(zlesamopoczucieODP)
        #         speak(losowa)
        #         zlydzien=getText()
        #         if 'nie' in zlydzien:
        #             speak("rozumiem.")
        #         elif 'tak' in zlydzien:
        #             speak("jak w takim razie mogę panu pomóc?")
        #             curr=getText()
        if len(if_Exists(aktualna,Wykryj)):         
            #Losowanie odpowiedzi do tak i nie oraz powitania
            losowa6=random.choice(odpowiedzitak)
            losowa7=random.choice(odpowiedzinie)
            rand=random.choice(powitania)
            speak(rand)

            #boolean
            warunek=False
            while warunek==False:
                warunek=True
                curr=getText()
                if len(if_Exists(curr,Zapisz)):
                    z=curr.lower().split(''+if_Exists(curr,Zapisz)[0]+'')[1]
                    speak("Zapisuję do notatnika.")
                    print("Zapisuję do notatnika.")
                    f2=open(Notatnik,'a',encoding='utf8')
                    f2.write(data+"\n"+z+"\n")
                    f2.close()
                elif len(if_Exists(curr,Usun)):
                    speak("Czy napewno chcesz usunąc ostatnią notatke?")
                    odpowiedz=getText()
                    if 'nie' in odpowiedz:
                        speak("okej")
                        print("okej")
                    else:
                        speak("Usuwam z pliku notatke: ")
                        print("Usuwam z pliku notatke: ")
                        f2=open(Notatnik,"r+")
                        linie2=f2.readlines()
                        speak(linie2[-1])
                        linie2.pop(-1)
                        f2.close()
                elif len(if_Exists(curr,Odczytywanie_ostatniej)):
                    speak("Ostatni zapis to:    ")
                    f2=open(Notatnik,'r')
                    linie2=f2.readlines()
                    speak(linie2[-1])
                    f2.close()
                elif len(if_Exists(curr,przegladarka)):
                    z2=curr.lower().split(''+if_Exists(curr,przegladarka)[0]+''[1])
                    driver.get(google+z2)
                elif len(if_Exists(curr,youtube)):
                    z=curr.lower().split(''+if_Exists(curr,youtube)[0]+'')[1]
                    speak("Rozumiem, włączam "+z+" na youtubie")
                    driver.get(yt+z)
                    time.sleep(4)
                    findByXpath('/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a').click()
                    findByXpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a').click()
                    driver.get(findByXpath('//*[@id="thumbnail"]').get_attribute("href"))
                elif len(if_Exists(curr,godzina1)):
                    speak(godzina)
                    print(godzina)
                elif len(if_Exists(curr,dzien)):
                    speak(data)
                    print(data)
                elif len(if_Exists(curr,imie_bota)):
                    speak('Mam na imię jarvis i zostałem stworzony przez pana Jakuba.')
                # elif len(if_Exists(curr,informacje_o_bocie)):
                #     speak(data)
                #     print(data)
                # elif len(if_Exists(curr,mozliwosci)):
                #     speak(data)
                #     print(data)
                elif len(if_Exists(curr,pogoda)):
                    print("szukam...")
                    user_api='fb0ce648492914de5c8f39d358764439'
                    location="Wejherowo"
                    complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
                    api_link=requests.get(complete_api_link)
                    api_data=json.loads(api_link.text)
                
                    print(api_data)
                    print("\n")
                    temp=api_data["main"]["temp"]
                    temp=temp-273.15
                    temp1=math.floor(temp)
                    print(temp1)
                    if temp1==1 or temp1==-1:
                         speak(str(temp1)+" stopień celsujsza.")
                    elif temp1>1 and temp1<=4 or temp1<-1 and temp1>=-4:
                         speak(str(temp1)+" stopnie celsujsza.")
                    else:
                         speak(str(temp1)+" stopni celsujsza.")
                elif len(if_Exists(curr,piosenkilosowe)):
                    speak("Co mam włączyć?")
                    curr2=getText()
                    if 'nie wiem' in curr2 or 'znajdź' in curr2 or 'wybierz' in curr2:
                        speak("W porządku, spróbuję coś zanaleźć.")
                        randomsong=random.choice(p)
                        driver.get(randomsong)
                        time.sleep(3)
                        findByXpath('/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a').click()
                    else:
                        z1=curr2.lower().split(''+if_Exists(curr2,youtube)[0]+'')[1]
                        speak("Rozumiem, włączam "+z1+" na youtubie")
                        driver.get(yt+z1)
                        time.sleep(4)
                        findByXpath('/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div[2]/div[5]/div[2]/ytd-button-renderer[2]/a').click()
                        findByXpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a').click()
                        driver.get(findByXpath('//*[@id="thumbnail"]').get_attribute("href"))
                elif len(if_Exists(curr,zglosnienie)):
                    speak("Podgłaśniam system")
                    count=0
                    while count<10:
                        py.press('volumeup')
                        count+=1
                elif len(if_Exists(curr,sciszenie)):
                    count=0
                    speak("ściszam system")
                    while count<10:
                        py.press('volumedown')
                        count+=1
                elif len(if_Exists(curr,vsc)):
                    speak("Rozumiem, otwieram visual studio code.")
                    os.system(visualstudiocode)
                    losowa=random.choice(vscOdp)
                    speak(losowa)
                    print(losowa)
                elif len(if_Exists(curr,Dowidzenia)):
                    speak("miłego dnia")
                    break
                elif len(if_Exists(curr,wchodzenienalibrusa)):
                    losowa=random.choice(odpowiedziproste)
                    speak(losowa)
                    driver.get(librus)
                    time.sleep(4)
                    findByXpath('/html/body/nav/div/div[3]/div[2]/div[2]/a/i').click()
                    findByXpath('/html/body/nav/div/div[3]/div[2]/div[2]/div/div/div[2]/a[2]').click()
                    time.sleep(2)
                    findByXpath('/html/body/main/div/div/div/div[1]/div[3]/div[1]/div[1]/input').send_keys('7477547u')
                    findByXpath('/html/body/main/div/div/div/div[1]/div[3]/div[2]/div[1]/input').send_keys('')
                    findByXpath('/html/body/main/div/div/div/div[2]/button').click()
                elif len(if_Exists(curr,dzieki)):
                    dziekowanie=linie10[1].split(',')
                    losowa=random.choice(dziekowanie)
                    speak(losowa)
                    print(losowa)
                    
                    
                else:
                    speak("Niestety nie rozumiem, czy mógłbyś powtórzyć?")
                    warunek=False
                
            # else:
            #     z=curr.lower().split(''+if_Exists(curr,Wykryj)[0]+'')[1]
            #     w.get(chrome).open('https://www.google.com/search?q='+curr)
        # elif len(if_Exists(aktualna,Dowidzenia)):
        #     speak("miłego dnia")
        #     break
        # elif len(if_Exists(aktualna,dzieki)):
        #         dziekowanie=linie10[1].split(',')
        #         losowa=random.choice(dziekowanie)
        #         speak(losowa)
        #         print(losowa)
        #         speak("Proszę bardzo")
        #         break
        
        
        


