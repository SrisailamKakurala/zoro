# Greet the user according to the time

import datetime
from utils.Speaker import speak

# current time in hour (24 hours format)
time = datetime.datetime.now().hour

def greet():
    if time > 0 and time < 12:
        speak("Good Morning BOSS")
    elif time >= 12 and time < 18:
        speak("Good Afternoon BOSS")
    else:
        speak("Good Evening BOSS")
    