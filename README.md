# Requirements

In order to run this script, you'll need to have the following libraries installed:

1. `speech_recognition`: This library is used to convert speech to text.
2. `textblob`: This library is used for processing textual data, providing simple API for diving into common natural language processing (NLP) tasks.
3. `sounddevice`: This library provides an interface to PortAudio, the cross-platform audio I/O library.
4. `scipy`: Specifically the `wavfile` module from `scipy` is used to read and write .wav files.
5. `pyttsx3`: An offline, Text to Speech library which works without internet connection and is compatible with both Python 2 and 3.
6. `pyaudio`: This is used for audio I/O.
7. `wave`: This is used for reading and writing .wav files.
8. `pygame`: A set of Python modules designed for writing video games, but useful for any multimedia project.
9. `playsound`: This library is used for playing sound files.

You can install these using pip:

```
pip install speechrecognition textblob sounddevice scipy pyttsx3 pyaudio wave pygame playsound
```

# README

This script provides a command-line interactive assistant, Solara, which has the following capabilities:

1. Text to Speech: Converts user input text to speech.
2. Speech to Text: Converts user's spoken words into text and displays it in the terminal.
3. Recording tool: Records user's voice and saves it as a .wav file, and then plays it back.
4. Spellcheck tool: Checks the spelling of a user input text and suggests corrections.

## Usage

Start the script with Python 3. Once Solara has introduced itself, you can choose a number from 1-5 and press enter to select an option.

1. Start Text to Speech: You will be prompted to enter some text, which will then be spoken aloud by the system.
2. Start Speech to Text: Solara will listen to your speech and display it as text in the terminal.
3. Start Recorder tool: Solara will record your voice for a predetermined duration and save it as a .wav file, then play it back.
4. Start spellcheck tool: You will be prompted to enter some text, which will then be checked for spelling errors. If any are found, the corrected text will be displayed.
5. Exit: Exit the program.

Note: You'll need a working microphone for the speech to text and recording functionalities.