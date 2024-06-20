import webbrowser
from utils.Speaker import speak


def open_youtube_channel():

        channel_uri = 'https://www.youtube.com/@Nobluffcoder-ssl/featured'
        webbrowser.open(channel_uri)
        speak("Opening youtube channel")
        
        
def open_channel_analytics():

        studio_uri = 'https://studio.youtube.com/channel/UCUwC0EfSrHJ6rocVcTblDTg/editing/sections'
        webbrowser.open(studio_uri)
        speak("Opening channel analytics")