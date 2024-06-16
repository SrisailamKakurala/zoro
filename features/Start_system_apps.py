import pyautogui as controller
import time

def open(query):
    query = query.replace('open', '').replace('start', '').strip()
    print(f"Trying to open: {query}")
    
    controller.hotkey('win') # Press the 'win' key
    time.sleep(1)
    controller.typewrite(query) # Type the query
    controller.press('enter') # Press 'enter' to execute the command
    return query




    