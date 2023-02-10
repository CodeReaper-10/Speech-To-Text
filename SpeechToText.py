import speech_recognition as sr
import time

rec = sr.Recognizer()

with sr.Microphone() as mic:
    print('You can start talking now...')
    audio = rec.listen(mic)
    print('Time\'s up!')

try:
    print('Text: ' + rec.recognize_google(audio))
except:
    print('It just exploded!')

time.sleep(10)
