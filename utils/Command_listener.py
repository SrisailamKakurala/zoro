import speech_recognition as sr


# Initialize the recognizer
recognizer = sr.Recognizer()


def listen_query(device_index):
    
    with sr.Microphone(device_index) as source:
        recognizer.adjust_for_ambient_noise(source)
        print(f"Listening on device {device_index if device_index is not None else 'default microphone'}...")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Could not understand the audio")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""

