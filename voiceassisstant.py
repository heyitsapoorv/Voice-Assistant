
''' A SIMPLE VOICE ASSISSTANT'''

import pyttsx3 
import matplotlib.pyplot as plt

import speech_recognition as sr 
import datetime
import wikipedia
import os


engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# print(voices[0].id)
# engine.setProperty('voice', voices[0].id)


def speak(word):
    engine.say(word)
    engine.runAndWait()
# voices = converter.getProperty('voices') 
# for voice in voices: 
    # to get the info. about various voices in our PC  
    # print("Voice:") 
    # print("ID: %s" %voice.id) 
    # print("Name: %s" %voice.name) 
    # print("Age: %s" %voice.age) 
    # print("Gender: %s" %voice.gender) 
    # print("Languages Known: %s" %voice.languages)

def greetings():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Boss!. Please tell me how may I help you")  
    
def email(a,b):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', a, b)
    server.close()
    
def command():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.3
        r.energy_threshold =350
        r.phrase_threshold = 0.2
        r.non_speaking_duration = 0.3 
        word = r.listen(source)

    try:
        print("Comprehending...")    
        words= r.recognize_google(word, language='en-in')
        print("You said:",words)

    except:
        print("I Didn't Get that,say that again please...")  
        return "None"
    return words


if __name__ == "__main__":
    greetings()
    command()

    while True:
          
        query = command().lower() 
        if 'wikipedia' in query: 
            speak('Searching') 
            query = query.replace("wikipedia", "") 
            results = wikipedia.summary(query, sentences = 2) 
            speak("According to Wikipedia") 
            print(results) 
            speak(results) 
         
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif "close youtube" in comm:
            speak("closing it")
            os.system("taskkill /f /im chrome.exe")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif "close google" in comm:
            speak("closing it")
            os.system("taskkill /f /im chrome.exe")
        elif 'email to apoorv' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "apoorvupadhyay1999@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("There is Some Error!!")
        elif 'shutdown' in query:
            speak("Activating all system shutting down sequence ; Have a nice day sir, good bye")
            os.system('shutdown -s)
                      
    
        else:
            speak("Can you speak it again sir")
                
#     speak("Boss. Please tell me how may I help you")

