from speak import *
import datetime
import speech_recognition as sr

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,50)

    try:
        speak("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')

    except Exception :   
        speak("Say that again please...")  
        return "None"
    return query 

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Hello Sir!Good Morning!")

    elif 12 <= hour < 18:
        speak("Hello Sir!Good Afternoon!")   

    else:
        speak("Hello Sir!Good Evening!")  

    speak("How can i help you")

def startup():
    speak("Initializing Jarvis")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Caliberating and examining all the core processors")
    speak("Checking the internet connection")
    speak("All drivers are up and running")
    speak("All systems have been activated")
    speak("assistant onilne")  
    
startup()
wishMe()
takeCommand()   