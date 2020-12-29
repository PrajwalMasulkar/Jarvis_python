import pyttsx3

engine = pyttsx3.init()
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Hello! This is python assistant")