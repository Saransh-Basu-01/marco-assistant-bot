import speech_recognition as sr
import webbrowser
import pyttsx3
import openai 
import music_library
from dotenv import load_dotenv
import os
# Initialize the text-to-speech engine
engine = pyttsx3.init()
load_dotenv()
# OpenAI API Key (Replace 'your-api-key' with your actual API key)
openai.api_key = os.getenv("OPENAI_API_KEY")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def ask_chatgpt(question):
    """Fetches the answer from OpenAI's ChatGPT API"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": question}]
        )
        answer = response["choices"][0]["message"]["content"]
        return answer
    except Exception as e:
        return f"Error fetching response: {e}"

def processcommand(command):
    print(f"Processing command: {command}")
    command = command.lower()

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com/")
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com/")
    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com/")
    elif command.startswith("play"):
        try:
            song = command.split(" ")[1].capitalize()
            if song in music_library.music:
                link = music_library.music[song]
                speak(f"Playing {song}")
                webbrowser.open(link)
            else:
                speak(f"Sorry, I couldn't find the song '{song}' in the library.")
        except IndexError:
            speak("Please specify the song you want to play.")
    elif "shutdown" in command or "exit" in command:
        speak("Shutting down. Goodbye!")
        exit()
    elif "what is" in command or "explain" in command:
        speak("Let me find the answer for you.")
        answer = ask_chatgpt(command)
        print(f"Answer: {answer}")
        speak(answer)
    else:
        speak("I didn't understand the command. Please try again.")

if __name__ == "__main__":
    speak("Initializing Marco...")
    while True:
        r = sr.Recognizer()
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening for the wake word...")
                audio = r.listen(source, timeout=10, phrase_time_limit=5)
            word = r.recognize_google(audio)
            if word.lower() == "marco":
                speak("Yes boss, I'm listening.")
                with sr.Microphone() as source:
                    print("Marco active. Waiting for a command...")
                    audio = r.listen(source, timeout=10, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    processcommand(command)
        except sr.UnknownValueError:
            print("I didn't catch that. Could you repeat?")
            speak("I didn't catch that. Could you repeat?")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            speak("Sorry, there seems to be an issue with the speech recognition service.")
        except Exception as e:
            print(f"Error: {e}")
            speak("An error occurred. Please try again.")
