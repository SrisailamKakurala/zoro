#### DRIVER FILE

from utils import Check_internet, Speaker, Recognizer, Greet, Command_listener
from assistants.Onine_assistant import online_assistant
from features.Start_system_apps import open


if __name__ == "__main__":
    
    online_assistant = online_assistant()
    
    # greet the user
    Greet.greet()
    
    # check for internet connection
    if Check_internet.check_internet():
        while True:
            speech = Command_listener.listen_query()
            if "jarvis" in speech or 'hey' in speech:
                Speaker.speak("Yes, how can I help you?")
                query = Recognizer.recognize()
                
                if 'open' in query or 'start' in query:
                     app = open(query)
                     Speaker.speak(f"opening {app}")
                else:
                    Speaker.speak("sorry, Unable to understand command")
        
            
                
                
    else:
        Speaker.speak("Please connect to the internet To USE me")
        # offline assistant code goes here