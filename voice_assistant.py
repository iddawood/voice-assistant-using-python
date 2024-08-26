import pyttsx3
import speech_recognition as sr 
import webbrowser
import datetime
import pyjokes
import os
import time
import ecapture as ec


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speechtx("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speechtx("Good Afternoon Sir !")   
  
    else:
        speechtx("Good Evening Sir !")  
  
    assname =("raj 1 point o")
    speechtx("I am your Assistant")
    speechtx(assname)



def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to You.....")
        recognizer.adjust_for_ambient_noise(source)
      
        audio=recognizer.listen(source)
        try:
            print("recognizing...")
            data=recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Sorry, I could not Understand You!")
            return ''


def speechtx(x):
    engine= pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    print(x)
    engine.runAndWait()

if __name__=="__main__":
    wishMe()

    if sptext().lower()=="raj":


            while True:

                    data1=sptext().lower()

                    if "your name" in data1:
                        name=" my name is raj "
                        speechtx(name)

                    elif "old are you" in data1:
                        age="i am ten tear old"
                        speechtx(age)

                    elif "time" in data1:
                        time_str=datetime.datetime.now().strftime("%I%M%p")
                        speechtx(f"Sir, the time is {time_str}")

                    elif "youtube" in data1:
                        speechtx("Here you go to youtube\n")
                        webbrowser.open("https://www.youtube.com/")

                    elif "wikipedia" in data1:
                        speechtx("Here you go to wikipedia\n")
                        webbrowser.open("https://www.wikipedia.org/")

                    elif 'open stack overflow' in data1:
                        speechtx("Here you go to Stack Over flow.Happy coding")
                        webbrowser.open("https://stackoverflow.com/") 


                    elif 'google' in data1:
                        speechtx("Here you go to google\n")
                        webbrowser.open("https://google.com")

                    elif "camera" in data1 or "take a photo" in data1:
                        speechtx("Here you go to google\n")
                        ec.capture(0, "Jarvis camera ", "img.jpg")

                    elif "who made you" in data1 or "who created you" in data1: 
                        speechtx("I have been created by Dawood.")

                
                    elif "exit" in data1:
                        speechtx("thank you")
                        break
                    time.sleep(3)
    else:
        print("thaks")
