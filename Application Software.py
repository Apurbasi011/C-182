from tkinter import*
import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime
import subprocess

root = Tk()
root.geometry("500x500")
root.configure(background = "Light Blue")

label = Label(root, text = "Welcome To Your Personal Desktop Assistant", bg = "Light Blue", 
              font = ("Bahnschrift Light", 15,"bold"))
label.place(relx = 0.5, rely = 0.1, anchor = CENTER)

text_to_speech = pyttsx3.init()

def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()
    
def r_audio():
    speak("How Can I Help You....?")
    speech_recognisor = sr.Recognizer()
    with sr.Microphone() as source:
        audio = speech_recognisor.listen(source)
        voice_date = ''
        
        try:
            voice_data = speech_recognisor.recognize_google(audio, language = 'en-in')
            
        except sr.UnknownValueError:
            print("Please Repeat I Did Not Get That")
            speak("Please Repeat I Did Not Get That")
            r_audio()
    respond(voice_data)
    
def respond(voice_data):
    voice_data = voice_data.lower()
    print(voice_data)
    if "name" in voice_data:
        speak("My Name Is Apurbasi")
        print("My Name Is Apurbasi")
        
    if "time" in voice_data:
        speak("Current Time Is :")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)
        
    if "search" in voice_data:
        speak("Opening Google")
        print("Opening Google")
        webbrowser.get().open("https://google.com")
        
    if "videos" in voice_data:
        speak("Opeaning Youtube")
        print("Opening Youtube")
        webbrowser.get().open("https://youtube.com")
        
    if "text editor" in voice_data:
        speak("Opening The App")
        print("Opening The App")
        subprocess.Popen(["notepad.exe"])
        
btn = Button(root, text = "Start", bg = "red3", fg = "white", padx = 10, pady = 1, 
             font = ("Arial", 11, "bold"), relief = FLAT, command = r_audio)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        
        
r_audio()
root.mainloop()
            

