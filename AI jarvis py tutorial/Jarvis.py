from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
print(">> Starting The Jarvis : Wait For Few Seconds.")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> Starting The Jarvis : Wait For Few seconds More")

def MainExecution():

    Speak("Hello Sir")
    Speak("I Am Jarvis, I am Ready To Assist You Sir.")

    while True:

        Data = MicExecution()
        Data = str(Data)

        if "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
            Reply = QuestionsAnswer(Data)

        else:

            Reply = ReplyBrain(Data)
            Speak(Reply)

def ClapDetect():
    
    query = Tester()
    if "True-Mic" in query:
        print("")
        print(">> Clap Detected!! >>")
        print("")
        MainExecution()
    else:
        pass

ClapDetect() 
