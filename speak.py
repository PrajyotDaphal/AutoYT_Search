import pyttsx3

def speak(Text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices[0].id)
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate',160)
    print(f"A.I : {Text}")
    engine.say(text=Text)
    engine.runAndWait()

