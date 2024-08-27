import pyttsx3

text = 'Я отвечаю за благополучие моих граждан, за установление порядка и справедливости, за обеспечение безопасности и процветания в обществе. Я стремлюсь к развитию экономики, социальной справедливости и укреплению моей авторитетности как главного института власти в стране. Я - защитник и покровитель общества, и моя миссия заключается в том, чтобы обеспечить моим гражданам лучшую жизнь. Ваши предположения?'
tts = pyttsx3.init()
rate = tts.getProperty('rate')  # Скорость произношения
tts.setProperty('rate', 180)

volume = tts.getProperty('volume')  # Громкость голоса
tts.setProperty('volume', 0.9)

voices = tts.getProperty('voices')

# Задать голос по умолчанию
tts.setProperty('voice', 'ru')

# Попробовать установить предпочтительный голос
for voice in voices:
    if voice.name == 'Anna':
        tts.setProperty('voice', voice.id)

tts.say(text)
tts.runAndWait()