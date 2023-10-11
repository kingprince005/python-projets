import pyttsx3
import speech_recognition as sr
import datetime
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voicees[0].id)
engine.setProperty('voices',voices[0].id)

#text to speech
def speak(Audio):
    engine.say(Audio)
    print(Audio)
    engine.runAndWait()

#convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        Audio = r.listen(source,timeout=2,phrase_time_limit=5)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(Audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again please...")
        return "none"
    return query

#to wish
def wish():
    hour = (datetime.datetime.now().hour)
    
    if hour>=8 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis sir. please tell me how can i help you")


if __name__== "__main__":
    takecommand()
    speak("this is advanced jarvis")
wish()
while True:

    query = takecommand().lower()

    #logic building for tasks

    if "open notepad" in query:
        npath = "C:\\Users\\hp\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessorie\\notepad.exe"
        os.startfile(npath)
    