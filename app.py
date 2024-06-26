#### DRIVER FILE

from threading import Thread
from utils import Check_internet, Speaker, Recognizer, Greet, Command_listener, Code_writer
from assistants.Onine_assistant import online_assistant
from features.Start_system_apps import open, close
from utils.get_active_input_device import get_device_index
from features.say_time import say_time
from features.open_custom_sites import *
from assistants.api import code_generator, text_generator
from features.battey_status import battery_alert, battery_life
from features import random_jokes, news, youtube_search, music, google_search, search_images, todolist

def main():
        # check for internet connection
        if Check_internet.check_internet():
            # check if user is using a bluetooth device
            device_index = get_device_index()
            while True:
                battery_alert()
                speech = Command_listener.listen_query(device_index)
                if ("rox" in speech) or ('xerox' in speech) or ("rok" in speech) or ("rocks" in speech) or ("iraqs" in speech) or ('hey' in speech):
                    Speaker.speak("Yes Boss!")
                    query = Recognizer.recognize(device_index)
                                     
                    
                    if query:
                        if 'youtube channel' in query:
                            open_youtube_channel()
                        elif 'channel analytics' in query:
                            open_channel_analytics()
                        elif ('open' in query) or ('start' in query):
                            app = open(query)
                            Speaker.speak(f"opening {app}")
                        elif 'voice' in query:
                            Speaker.speak("changing voice boss")
                            Speaker.change_voice()
                        elif 'close' in query:
                            close(query)
                        elif 'speak fast' in query:
                            Speaker.speak_fast()
                        elif 'speak slow' in query:
                            Speaker.speak_slow()
                        elif 'time' in query:
                            say_time()
                        elif 'code' in query:
                            Speaker.speak("on it boss")
                            res = code_generator.get_response(query)
                            Code_writer.write(res)
                            print(res)
                        elif 'battery life' in query:
                            battery_life()
                        elif 'joke' in query:
                            speak(random_jokes.joke())
                        elif 'news' in query:
                            speak(news.get_news())
                        elif 'youtube' in query:
                            youtube_search.utube_search()
                        elif 'google' in query:
                            google_search.google_search()
                        elif 'music' in query:
                            music.play_music()
                        elif 'images' in query:
                            search_images.images()
                        elif ('task' in query) and ('add' in query):
                            speak("what is the task")
                            task = Recognizer.recognize(0)
                            ack = todolist.add_reminder(task)
                            if ack:
                                speak("task added to todo")
                            else:
                                speak("please try again boss")
                        elif ('todo list' in query) or ('show' in query):
                            ack = todolist.show_todo()
                            if ack:
                                speak("opening todo")
                            else:
                                speak("please try again boss")
                        else:
                            res = text_generator.get_text_response(query)
                            Speaker.speak(res)
        

        else:
            Speaker.speak("Please connect to the internet To USE me")
            # offline assistant code goes here
            

if __name__ == "__main__":
    
    online_assistant = online_assistant()
    
    # greet the user
    Thread(target=Greet.greet()).start()
   
    Thread(target=main()).start()

    
    
    