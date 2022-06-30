from speak import *
import webbrowser as web 
import pywhatkit

def Youtubesearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    web.open(result)
    speak("This Is What I Found For Your Search .")
    pywhatkit.playonyt(term)
    speak("This May Also Help You Sir .")

Youtubesearch()    