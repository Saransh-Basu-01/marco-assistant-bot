import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
recognizer = sr.Recognizer()
engine = pyttsx3.init()
#this code is incomplete
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(command):
    print(f"Processing command: {command}")
    # Add custom logic to handle the command here
    if "open google" in command.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open facebook" in command.lower():
        speak("opening facebook")
        webbrowser.open("https://www.facebook.com/")
    elif "open youtube" in command.lower():
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com/")
    elif command.lower().startswith("play"):
        song=command.lower().split(" ")[1]
        link=music_library.music[song]
        webbrowser.open(link)
    else:
        speak("I didn't understand the command.")

if __name__ == "__main__":
    speak("Initializing Marco...")
    # Listen for the wake word "Marco"
    while True:
        r = sr.Recognizer()
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if word.lower() == "marco":
                speak("Yes boss")
                # Listen for command
                with sr.Microphone() as source:  # Fixed typo here
                    print("Marco active")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processcommand(command)
        except Exception as e:
            print(f"Error: {e}")
