import encodings
import sys

from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import random
import json
from neuralintents import BasicAssistant


with open('intents.json', 'r', encoding='utf8') as file:
    data = json.load(file)
    assistant = BasicAssistant(data)
assistant.fit_model(epochs=20)
assistant.save_model()

tts = pyttsx3.init()
rate = tts.getProperty('rate')  # Скорость произношения
tts.setProperty('rate', 160)

volume = tts.getProperty('volume')  # Громкость голоса
tts.setProperty('volume', 1.2)

voices = tts.getProperty('voices')

# Задать голос по умолчанию
tts.setProperty('voice', 'ru')

# Попробовать установить предпочтительный голос
for voice in voices:
    if voice.name == 'Anna':
        tts.setProperty('voice', voice.id)




model = Model(r"vosk-model-small-ru-0.22")  # полный путь к модели
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=16000,
    input=True,
    frames_per_buffer=16000
)
stream.start_stream()

def greeting(vvod):
    global f
    text = vvod.split('"')[3]
    # print(assistant.process_input(text))
    if text != "":
        print(text)

    if 'джарвис' in vvod and f == 0:
        tts.say("да сэр?")
        tts.runAndWait()
        f = 1

    if 'text' in vvod and f == 1:
        if 'протокол сон' in vvod:
            tts.say('до скорого сэр!')
            tts.runAndWait()
            sys.exit(0)
        if text != 'джарвис':
            tts.say(assistant.process_input(text))
            tts.runAndWait()
            f = 0
    #elif f == 1:
    #    f = 0


f = 0
while True:
    data = stream.read(2500, exception_on_overflow=False)
    if len(data) == 0:
        break

    result = rec.Result() if rec.AcceptWaveform(data) else rec.PartialResult()
    greeting(result)






print(rec.FinalResult())