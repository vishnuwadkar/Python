import speech_recognition as sr     #to simplify usage of speechrecognition, use 'as'
import webbrowser   #module to open web browser using python
import pyttsx3      # to convert text to speech
import musicLib

recognizer = sr.Recognizer()    #recognizer object to recognize speech
engine = pyttsx3.init()           #text to speech object to convert text to speech

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):  #function for processing the command
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open netflix" in c.lower():
        webbrowser.open("https://netflix.com")
    elif "open gmail" in c.lower():
        webbrowser.open("https://gmail.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    #for playing songs
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLib.music[song]
        webbrowser.open(link)

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        #Listen for the wake word 'Jarvis'

        # obtain audio from the microphone
        r = sr.Recognizer()
        print("recognizing...")
        # recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            command = r.recognize_google(audio)
            if "jarvis" in command.lower():
                speak("Ya")
                #listen for the command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            print("Error: {0}".format(e))