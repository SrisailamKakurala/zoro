import datetime
from utils.Speaker import speak

def say_time():
    current_hour = datetime.datetime.now().hour
    current_min = datetime.datetime.now().minute
    
    if(current_hour >= 0 and current_hour < 12):
        speak(f"it's {current_hour} , {current_min} AM, boss")
    else:
        hour = current_hour - 12;
        # when the time is b/w 12 and 1
        if(hour == 0):
            speak(f"it's 12 , {current_min} PM, boss")
            
        # when the time is beyond 1
        speak(f"it's {hour} , {current_min} PM, boss")
    
    
