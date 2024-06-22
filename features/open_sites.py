import webbrowser
from utils.Speaker import speak
from threading import Thread

def open_youtube_channel():

        channel_uri = 'https://www.youtube.com/@Nobluffcoder-ssl/featured'
        Thread(target= webbrowser.open(channel_uri)).start()
        Thread(target=speak("Opening youtube channel")).start()
        
        
        
def open_channel_analytics():

        studio_uri = 'https://studio.youtube.com/channel/UCUwC0EfSrHJ6rocVcTblDTg/editing/sections'
        Thread(target=webbrowser.open(studio_uri)).start()
        Thread(target=speak("Opening channel analytics")).start()