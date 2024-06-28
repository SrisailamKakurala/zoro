import pywhatkit as kit
import webbrowser
from utils import Speaker, Recognizer


def images():
    Speaker.speak("what do u want to search")
    search = Recognizer.recognize(0)
    if search == 'nothing':
        webbrowser.open("www.google.com")
    else:
        webbrowser.open(f'https://www.bing.com/images/search?q={search}+images&form=HDRSC3&first=1')
        Speaker.speak("searching for images")
