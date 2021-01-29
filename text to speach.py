import  pyttsx3
from pyttsx3 import voice

engine = pyttsx3.init()
voices = engine.getProperty(('voices'))
engine.setProperty('voice',voices[1].id)

engine.say('Hello raj sir, how may I help you, sir.')
engine.runAndWait()