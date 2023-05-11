import speech_recognition as sr
import textblob
import sounddevice as sd
from scipy.io.wavfile import write, read
import pyttsx3
import pyaudio
import wave
import pygame
from playsound import playsound
listener = sr.Recognizer()
# Set the duration of the recording in seconds
duration = 5  # for example

# Set the sampling rate
sampling_rate = 44100
text_speech = pyttsx3.init()

menu1 = input("Hello User,\n I am your Project Assistant, Solara, please choose a number and press enter.\n"
      "1. Start Text to Speech\n"
      "2. Start Speech to Text\n"
      "3. Start Recorder tool\n"
      "4. Start spellcheck tool\n"
      "5. Exit\n")

##Listen to speech creates Text in terminal
def start_speech_to_text():
    on = True
    while on == True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                print(command)
                on = False
                break
        except:
            pass
    return command



## Create text and output to speech
def start_text_to_speech():
    text = input("Enter text to be spoken: ")
    text_speech.say(text)
    text_speech.runAndWait()
    return text


## Record and Playback with function
def record_and_playback():
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Reading Microphone as source
    # Listening the speech and store in audio_text variable
    with sr.Microphone() as source:
        print("Recording...")
        audio_text = r.listen(source)
        print("Recording finished. Saving...")
        with open("output.wav", "wb") as file:
            file.write(audio_text.get_wav_data())
        playsound("output.wav")


def correct_spelling():
    text = input("Enter text to be checked: ")
    blob = textblob.TextBlob(text)
    corrected_text = str(blob.correct())
    print("Corrected text: " + corrected_text)
    return corrected_text

## Create menu options
game  = "Running"

while game == "Running":
    if menu1 == "1":
        start_text_to_speech()
        menu1 = input("Hello User,\n I am your Project Assistant, Solara, please choose from the following menu items.\n"
      "1. Start Text to Speech\n"
      "2. Start Speech to Text\n"
      "3. Start Recorder tool\n"
      "4. Start spellcheck tool\n"
      "5. Exit\n")
    elif menu1 == "2":
        start_speech_to_text()
        menu1 = input("Hello User,\n I am your Project Assistant, Solara, please choose from the following menu items.\n"
      "1. Start Text to Speech\n"
      "2. Start Speech to Text\n"
      "3. Start Recorder tool\n"
      "4. Start spellcheck tool\n"
        "5. Exit\n")
    elif menu1 == "3":
        record_and_playback()
        menu1 = input("Hello User,\n I am your Project Assistant, Solara, please choose from the following menu items.\n"
      "1. Start Text to Speech\n"
      "2. Start Speech to Text\n"
      "3. Start Recorder tool\n"
      "4. Start spellcheck tool\n"
    "5. Exit\n")
    elif menu1 == "4":
        correct_spelling()
        menu1 = input("Hello User,\n I am your Project Assistant, Solara, please choose from the following menu items.\n"
      "1. Start Text to Speech\n"
      "2. Start Speech to Text\n"
      "3. Start Recorder tool\n"
      "4. Start spellcheck tool\n"
            "5. Exit\n")
    elif menu1 == "5":
        print("Thank you for using Solara, goodbye.")
        game = False
    else:
        print("Invalid input, please try again.")
        menu1 = input("Hello User,\n I am your Project Assistant, Solara, please choose from the following menu items.\n"
      "1. Start Text to Speech\n"
      "2. Start Speech to Text\n"
      "3. Start Recorder tool\n"
      "4. Start spellcheck tool\n"
                      "5. Exit\n")
