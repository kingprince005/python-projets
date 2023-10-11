import speech_recognition as sr
from googletrans import Translator

# 1. Listen : Hindi or English

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en")

    except:
        return ""
    
    query = str(query).lower()
    return query

Listen()
# 2. Translation

def TranslationHinToEng(Text):

    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"you : {data}.")
    return data 

# 3. Connect
def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data