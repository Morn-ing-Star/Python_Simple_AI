import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init(driverName='sapi5')
# engine = pyttsx3('sapi5')
voices= engine.getProperty('voices')
voices[1].id
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")
        
        
    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")
        

    else:
        print("Good Evening!")
        speak("Good Evening!")
        
    
    speak("I am Cosmos Sir. How may I Help you ? ")

def takeCommand():
    # It Take voice from user
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.energy_threshold = 100
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        print("pardon! , Say that Again Please..... ")
        return "None"
    return query

def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ronojoy1092002@gmail.com', 'cjnwmbqvnxaiwesa')
    server.sendmail('hopeuknow2022@gmail.com', to , content)
    server.close()
    

if __name__ == "__main__":
    wishMe()
    while True:
      query = takeCommand().lower()
     
      #  Logic for executing task on query
      if 'wikipedia' in query:
          speak('Searching Wikipedia......')
          query = query.replace("wikipedia" , "")
          results = wikipedia.summary(query , sentences=2)
          speak("According to Wikipedia")
          speak(results)
        
      elif 'open youtube' in query:
          webbrowser.open("youtube.com")
          
      elif 'what are you' in query:
          speak("Hello, My name is Cosmos , I am your Personal Assistant and i will help you as per your need but limited because i am not so advance like other AI's")
      elif 'about yourself' in query:
          speak("Hello, My name is Cosmos , I am your Personal Assistant and i will help you as per your need but limited because i am not so advance like other AI's")
      elif 'who are you' in query:
          speak("I am Cosmos , I am a Personal Assistant ")    
          
      elif 'open google' in query:
          webbrowser.open("google.com")
          
      elif 'play music' in query:
          music_dir = 'D:\Projects_Codes\Python\Voice Assistant Using Python\music_dir'
          songs = os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir , songs[0]))
          
      elif 'thank you' in query:
          speak("It's my pleaser Sir...")
      elif 'thanks' in query:
          speak("It's my pleaser Sir...")
          
      elif 'the time' in query:
          strTime = datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"Sir The time is : {strTime}")
      elif 'time' in query:
          strTime = datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"Sir The time is : {strTime}")
          
      elif 'open code' in query:
          codePath = "C:\\Users\\Rj\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
          os.startfile(codePath)
          
      elif 'email to morning star' in query:
            try:
              speak("What should I say?")
              content = takeCommand()
              to = "hopeuknow2022@gmail.com"
              sendEmail(to , content)
              speak("Email has been sent!")
              print(("Email has been sent!"))
            except Exception as e:
             print(e)
             speak("Sorry Sir , I am not able to sent mail...")

          
           

    
    



