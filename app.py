#### DRIVER FILE

from utils import Check_internet, Speaker, Recognizer, Greet
from assistants.Offline_assistant import offline_assistant
from assistants.Onine_assistant import online_assistant


if __name__ == "__main__":
    
    # greet the user
    Greet.greet()
    
    # check for internet connection
    if Check_internet.check_internet():
        while True:
            query = Recognizer.recognize()
            if 'voice' in query:
                Speaker.change_voice()
                
    else:
        Speaker.speak("Please connect to the internet To USE me")