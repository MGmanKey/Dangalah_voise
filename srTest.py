# 5 9 18 19 20
import speech_recognition as sr

def record_volume():
    r = sr.Recognizer()
    with sr.Microphone(device_index = 9) as source:
        print('Настраиваюсь.')
        r.adjust_for_ambient_noise(source, duration=0.5) #настройка посторонних шумов
        print('Слушаю...')
        audio = r.listen(source)
    print('Услышала.')
    print(audio)
    try:
        #query = r.recognize_google_cloud(audio, language = 'ru-RU')
        query = r.recognize_vosk(audio, language = 'ru-RU')
        text = query.lower()
        print(f'Вы сказали: {query.lower()}')
    except Exception as exc:
        print(f'Error\n{exc}')

while True:
    record_volume()
