import pyttsx3

# creating an instance of pyttsx3
jarvis = pyttsx3.init()

# variable properties
rate = 150
voice_male = jarvis.getProperty('voices')[0].id
voice_female = jarvis.getProperty('voices')[1].id

# Default voice selection (change this to 'male' or 'female' as desired)
default_voice = 'male'

# Load saved voice selection
try:
    with open('voice_state.txt', 'r') as file:
        default_voice = file.read().strip()
except FileNotFoundError:
    pass  # Use default voice if file doesn't exist

# Set initial voice based on loaded state
if default_voice == 'male':
    voice1 = True
    voice2 = False
    jarvis.setProperty('voice', voice_male)
else:
    voice1 = False
    voice2 = True
    jarvis.setProperty('voice', voice_female)

# methods
def speak(content):
    jarvis.say(content)
    jarvis.runAndWait()
    
def speak_fast():
    jarvis.setProperty('rate', rate + 30)
    speak("yes sir, i will speak fast")
    
def speak_slow():
    jarvis.setProperty('rate', rate)
    speak("yes sir, i will speak slow")
    
def change_voice():
    global voice1, voice2, default_voice
    
    if voice1:
        # if the male voice is active change to female voice
        jarvis.setProperty('voice', voice_female)
        voice1, voice2 = False, True
        default_voice = 'female'
        speak("Successfully changed the voice boss")
    else:
        # if the female voice is active change to male voice
        jarvis.setProperty('voice', voice_male)
        voice1, voice2 = True, False
        default_voice = 'male'
        speak("Successfully changed the voice boss")
    
    # Save the changed voice selection
    with open('voice_state.txt', 'w') as file:
        file.write(default_voice)
