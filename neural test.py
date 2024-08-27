from neuralintents import BasicAssistant
import json

with open('intents.json', 'r', encoding='utf8') as file:
    data = json.load(file)
    assistant = BasicAssistant(data)
assistant.fit_model(epochs=20)
assistant.save_model()

a = assistant.process_input("скажи привет")
print(a)
