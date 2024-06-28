import pywhatkit as kit
import webbrowser
from utils import Speaker, Recognizer


def utube_search():
    Speaker.speak("what do u want to search")
    search = Recognizer.recognize(0)
    if search == 'nothing':
        webbrowser.open("www.youtube.com")
    else:
        kit.playonyt(search)
        Speaker.speak("searching on youtube")
