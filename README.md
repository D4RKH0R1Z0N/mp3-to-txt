# MP3 to TXT Converter

### Installation

```
pip install SpeechRecognition
```

### Run

Go to The code and replace `file.mp3` to the mp3 file name you want to convert (with .mp3 at the end)

```
import speech_recognition as sr

def main():
    sound = "file.mp3" <--- Replace this value of this variable
    r = sr.Recognizer()

    with sr.AudioFile(sound) as source:
        r.adjust_for_ambient_noise(source)
        print("Converting Audio File to Text...
```
