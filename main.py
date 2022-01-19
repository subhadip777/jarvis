from random import random
from unittest import result
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import random
import pywhatkit as pw
import flask
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# engine.setProperty('voices',voices[1].id)
engine.setProperty('voices',voices[2].id)

# print(voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour= int (datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("good morning sir")
    elif hour >= 12 and hour <18:
        speak("good afternoon sir")
    else:
        speak("good evening garry")
    speak(" how can i help you sir?")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listneing.....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        print("say that again")
        return "none"
    return query





if __name__=="__main__":
    # wishme()
    
    while(True):
        query=takeCommand().lower()
        if "wikipedia" in query:
            speak("searching from wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            speak("opening yourube sir")
            webbrowser.open("youtube.com")
        elif "open facebook" in query:
            speak("opening facebook for you")
            webbrowser.open("facebook.com")
        elif "music from youtube" in query:
            # speak("from youtube or device sir?")
            # query2=takeCommand().lower()
            # if "youtube"in query2:
            #     speak("wish adds din't start bothering you ha ha ha")
            speak("playing a soothing music for you sir")
            webbrowser.open("https://www.youtube.com/watch?v=WMTTI2XYPWc",new=2,autoraise=True)
        elif " music from device" in query:
            music_dir='G:\\LOCAL DRIVE F\\রবীন্দ্র সঙ্গীত\\110 rabi'
            songs=os.listdir(music_dir)
            print(music_dir)
            # i=random(0,len(songs))
            # speak("playing a local music sir")
            os.startfile(os.path.join(music_dir,random.choice(songs)))
            
        elif "open gfg" in query:
            speak("opening sir")
            webbrowser.open("geeksforgeeks.org",new=2,autoraise=True)
        elif "open geeksforgeeks" in query:
            speak("opening sir")
            webbrowser.open("geeksforgeeks.org",new=2,autoraise=True)
        elif "open geeks for geeks" in query:
            speak("opening sir")
            webbrowser.open("geeksforgeeks.org",new=2,autoraise=True)
        elif "open codechef" in query:
            speak("opening sir")
            webbrowser.open("codechef.com",new=2,autoraise=True)
        elif "open whatsapp" in query:
            speak("opening sir")
            webbrowser.open("whatsapp.com")

        elif "hi jarvis" in query:
            wishme()
            query=takeCommand().lower()
        elif "hey jarvis" in query:
             wishme()
        elif "vs code" in query:
            os.startfile("C:\\Users\\User\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.")
        elif "sublime" in query:
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\sublime Text 3")
        else :
            if(query != "none"):
                speak("this is what i got from internet sir")
                pw.search(query)

            

        



        



