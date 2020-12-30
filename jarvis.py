import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import subprocess
import pyjokes

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

def jokes():
    speak(pyjokes.get_joke())


def wishme():
    speak("Welcome back sir!")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak("Good morning")
    elif hour >=12 and hour < 18:
        speak("Good afternoon")
    elif hour >=18 and hour <= 24:
         speak("Good evening")
    else:
        speak("Good night")

    speak("Friday at your service sir. How I can help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = "en-in")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"

    return query

if __name__ == "__main__":

    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences= 2)
            speak(result)
        elif "search in chrome" in query:
            speak("What should I search?")
            chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")

        elif "play songs" in query:
            songs_dir = "E:\pd\Music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[1]))

        elif "joke" in query:
            jokes()
