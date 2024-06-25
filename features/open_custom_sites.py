import webbrowser
from utils.Speaker import speak
from threading import Thread

def open_youtube_channel():

        uri = 'https://www.youtube.com/@Nobluffcoder-ssl/featured'
        Thread(target= webbrowser.open(uri)).start()
        Thread(target=speak("Opening youtube channel")).start()
        
        
def open_channel_analytics():

        uri = 'https://studio.youtube.com/channel/UCUwC0EfSrHJ6rocVcTblDTg/editing/sections'
        Thread(target=webbrowser.open(uri)).start()
        Thread(target=speak("Opening channel analytics")).start()
        

def open_college_website():
        
        uri = 'https://tkrcet.ac.in/'
        Thread(target=webbrowser.open(uri)).start()
        Thread(target=speak("Opening channel analytics")).start()