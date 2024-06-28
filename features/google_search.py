import pywhatkit as kit
import webbrowser
from utils import Speaker, Recognizer


def google_search():
    Speaker.speak("what do u want to search")
    search = Recognizer.recognize(0)
    if search == 'nothing':
        webbrowser.open("www.google.com")
    else:
        kit.search(search)
        Speaker.speak("searching on google")
