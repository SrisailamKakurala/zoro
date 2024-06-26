# recognizes the user speech

import speech_recognition as sr
from utils.Speaker import speak
from threading import Thread

# create an instance of speech_recognition
recognizer = sr.Recognizer()

def recognize(device_index):
    # determines the amount of silence required at the end of a phrase to consider the phrase complete
    recognizer.pause_threshold = 1
    with sr.Microphone(device_index) as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.3) # to differ bg noise and user speech
        Thread(target=print, args=("Listening...", )).start()
        query = recognizer.listen(source)
    
    
    # recognize the speech and convert to text
    if query:
        try:
            text = recognizer.recognize_google(query)
            print("User said: ", text)
            return text.lower()
        except sr.UnknownValueError:
            print("sorry, Unable to understand command")
            speak("sorry, Unable to understand command")
            return 'False'
        except sr.RequestError as e:
            print("Recognition request failed: ", e)
            speak("Recognition request failed")
            return 'False'
    