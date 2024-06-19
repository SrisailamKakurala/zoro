import pyautogui as controller
import time
import os
from utils.Speaker import speak
import psutil


def open(query):
    query = query.replace('open', '').replace('start', '').strip()
    print(f"Trying to open: {query}")
    
    controller.hotkey('win') # Press the 'win' key
    time.sleep(1)
    controller.typewrite(query) # Type the query
    controller.press('enter') # Press 'enter' to execute the command
    return query

    

def close(query):
    query = query.replace('close', '').strip().lower()

    process_found = False
    for proc in psutil.process_iter(['pid', 'name']):
        process_name = proc.info['name'].lower()
        if query in process_name or f"{query}.exe" in process_name:
            process_found = True
            try:
                os.system(f"taskkill /f /pid {proc.info['pid']}")
                speak(f"{query} terminated successfully")
                return
            except Exception as e:
                speak(f"Failed to terminate {query}: {e}")
                return

    if not process_found:
        speak(f"No running process found for {query}")



    