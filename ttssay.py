

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


tts.say("")
