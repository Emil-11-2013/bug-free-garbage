from operator import truediv

import speech_recognition as sr
import pyttsx3
from datetime import datetime

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()
    return text

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            command = r.recognise_google(audio)
            print("You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service")

    return ""

def respond_to_speech(text):
    if "hello" in text:
        speak("Hello")


    elif "hi" in text:
        speak("Hi")



    elif "whats ur name" in text:
        speak("My name is PYlexa")

    elif "how are you" in text:
        speak("As an AI assistant, i dont have feelings")

    elif "Whats the time" in text:
        speak(f"The time is {datetime.now().strftime('%I:%M %p')}")

    elif "exit" in text:
        speak("Goodbye")
        return False

    else:

        speak("Sorry, I did not understand you")

        return True

def main():

    speak("Hi there, I'm PYlexa")
    while True:
        command = get_audio()
        if command and not respond_to_speech(command):
            break

if __name__ == "__main__":
    main()