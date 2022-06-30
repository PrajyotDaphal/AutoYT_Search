from speak import *
from SpeechRecognition import *
from YoutubeSearch import *

if __name__ == "__main__":
    startup()
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

     # Logic for executing tasks based on query
        if 'youtube search' in query:
            Query = query.replace("jarvis","")
            query = Query.replace("youtube search","")
            Youtubesearch(query)