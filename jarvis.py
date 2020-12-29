import pyttsx3
import datetime

engine = pyttsx3.init()


voice=engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)
newVoiceRate = 145
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    speak("The current time is")
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():
    speak("Welcome back sir!")
    time()
    date()
    speak("Friday at your service sir.How I can help you?")

wishme()