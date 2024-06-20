#### DRIVER FILE

from utils import Check_internet, Speaker, Recognizer, Greet, Command_listener
from assistants.Onine_assistant import online_assistant
from features.Start_system_apps import open, close
from utils.get_active_input_device import get_device_index
from features.say_time import say_time
from features.open_sites import *
from assistants.api import code_generator, text_generator, image_response

def main():
        # check for internet connection
        if Check_internet.check_internet():
            # check if user is using a bluetooth device
            device_index = get_device_index()
            while True:
                speech = Command_listener.listen_query(device_index)
                if ("jarvis" in speech) or ('hey' in speech):
                    Speaker.speak("Yes, how can I help you?")
                    query = Recognizer.recognize(device_index)
                    
                    if 'youtube channel' in query:
                        open_youtube_channel()
                    elif 'channel analytics' in query:
                        open_channel_analytics()
                    elif ('open' in query) or ('start' in query):
                        app = open(query)
                        Speaker.speak(f"opening {app}")
                    elif 'voice' in query:
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
                        res = code_generator.get_response(query)
                    else:
                        res = text_generator.get_text_response(query)
                        Speaker.speak(res)
        
            
                
                
        else:
            Speaker.speak("Please connect to the internet To USE me")
            # offline assistant code goes here
            

if __name__ == "__main__":
    
    online_assistant = online_assistant()
    
    # greet the user
    Greet.greet()
    
    main()