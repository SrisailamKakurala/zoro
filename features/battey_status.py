import psutil
from utils.Speaker import speak


def get_battery_status():
    percent, seconds, plugged_in = psutil.sensors_battery()
    
    return percent, seconds, plugged_in


def battery_alert():
    percent, _, plugged_in = get_battery_status()
    
    low_battery_is_alerted = False
    full_battery_is_alerted = False
    
    if not low_battery_is_alerted:
        if percent <= 20 and not plugged_in:
            speak("Battery is low! Please plug in your charger.")
            low_battery_is_alerted = True
    
    if not full_battery_is_alerted:
        if percent == 100 and plugged_in:
            speak("Battery fully charged! you can unplug now")
            full_battery_is_alerted = True
        

def battery_life():
    _, seconds, _ = get_battery_status()
    hours = round((seconds/60)/60, 2)
    time_left = str(hours).split('.')
    speak(f"{time_left[0]} hours and {time_left[1]} minutes")
    