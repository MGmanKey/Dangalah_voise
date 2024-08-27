import sys
import threading
import tkinter as tk

import speech_recognition
import pyttsx3 as tts

from neuralintents import BasicAssistant


class Assistant:

    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self.speeker = tts.init()
        self.speeker.setProperty("rate", 150)

        self.assistant = BasicAssistant("intents.json",)
        self.assistant.fit_model()
        self.assistant.save_model()

        #self.root = tk.Tk()
        #self.lable = tk.Label(text="BOT", font=("Arial", 120, "bold"))
        #self.lable.pack()

        #threading.Thread(target=self.run_assistant).start()
        self.run_assistant()
        #self.root.mainloop()

    def run_assistant(self):
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = self.recognizer.listen(mic)

                    text = self.recognizer.recognize_google_cloud(audio)
                    text = text.lower()
                    print(text)
                    if "hey jake" in text:
                        #self.lable.config(fg="red")
                        print("es")
                        audio = self.recognizer.listen(mic)
                        text = self.recognizer.recognize_google_cloud(audio)
                        text = text.lower()

                        if text == "stop":
                            self.speeker.say("Bye")
                            self.speeker.runAndWait()
                            self.speeker.stop()
                            #self.root.destroy()
                            sys.exit(0)
                        else:
                            if text is not None:
                                response = self.assistant.process_input(text)
                                if response is not None:
                                    self.speeker.say(response)
                                    self.speeker.runAndWait()
                            #self.lable.config(fg="black")
            except Exception as exc:
                print(exc)
                #self.lable.config(fg="black")
                continue


Assistant()