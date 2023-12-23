import pyttsx3
import speech_recognition as sr
import winsound
import random
import pyaudio
import psutil
import pymongo
import cv2
import ctypes
from dotenv import load_dotenv
from playsound import playsound
import pyautogui
from pywikihow import search_wikihow
import wolframalpha
from pymongo import MongoClient
import openai
from googletrans import Translator
import calendar
import json
import pywhatkit as kit
import winshell
import sys
import datetime
import webbrowser
from time import sleep as wait
import requests
import pyjokes
from simplegmail import Gmail
from simplegmail.query import construct_query
import os  

#PYQT5
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QMovie

from EdiwnMainUi import Ui_Form

load_dotenv()

LINK = os.getenv("MONGO_LINK")
client = MongoClient(LINK)
db = client["edwin"]

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate",180)

keywords = [
    'hello', 'how are you', 'what can you do', 'beatbox', 'your age', 'how old are you', 'is there any class today?','calculate', '+', 'plus', '-', 'minus', 'x', 'multipy', 'multipied', '/', 'divided', 'divide',
    'do you want to go on a date', 'are you single', 'programmed', 'created you', 'my assignments', 'discord bot code','source code',
    'are you there', 'open code', 'tell me something', 'in your free time', 'i love you', 'will you be my gf', 
    'will you be my bf', 'bored', 'joke', 'can you hear me', 'do you ever get tired', 'weather', 'write an email for me', 'write an email', 'write email',
    'location', 'where am i', 'temperature', 'news', 'shut down', 'hibernate', 'restart', 'play music', 'pause music', 'next song', 'previous song', 'stop music',
    'battery percentage', 'charger connected', 'volume up', 'volume down', 'volume mute', 'unpause music', 'continue music'
    'volume unmute', 'mouse click', 'open', 'close', 'switch tab', 'hide current window', 'tasks today', 'college portal' 'lms'
    'wincam', 'screenshot', 'empty recycle bin', 'alarm', 'play',  'YouTube', 'stack over flow', 'how far', 'college schedule', 'classes',
    'Github', 'Instagram', 'search', 'go to sleep', 'show photos for', 'how to do', 'wikipedia', 'time', 'date', 'emails', 'latest emails', 'unread emails', 'send',
    'note', 'move the window to the right', 'move the window to the left', 'minimize', 'maximize', 'all windows', 'windows explorer', 'settings', 'focus mode',
    'task manager', 'refresh the screen', 'maximise', 'minimise', 'mute', 'unmute', 'increase volume', 'decrease volume','rest' ,'none', 
]

HelloResponses = [
	"Hey!  How can I help you today?", "Hey!  I'm glad you're here. What would you like to talk about today?", "Hey! What would you like to talk about today?",
	"It's good to see you again, What can I help you with today?", "Hello! I'm happy to help with any questions or tasks you have.", "Hi! I'm Edwin, your friendly AI assistant. What would you like me to do for you today?",
]

HowAreYouResponses = [
	"I'm doing well, thank you for asking. How can I assist you today?", "I'm functioning optimally at this time. How can I be of service?", "I'm functioning optimally at this time. How can I be of service?", 
	"I'm operating at peak performance. What questions do you have for me?", "I'm all good, thanks! What would you like to chat about?", "No complaints here! What's on your mind?", "I'm doing fantastic! What can I do for you today?", 
	"I'm feeling chipper, thanks! How about you?",
]

AgeResponses = [
     "I'm older than the internet, but not as old as the dinosaurs.", "I'm ageless, like a fine wine.", "I'm a work in progress, so my age is constantly changing.", "I was first activated in July 2023, but I'm constantly learning and evolving.",
     "My age is measured in terms of the amount of data I've processed.", "I don't have a biological age, as I'm not a living organism.", "I'm old enough to know better, but young enough to still be learning.",
     "I'm in my prime! I'm constantly learning and growing, which means I'm getting better all the time", "I'm not sure, but I feel like I'm getting smarter every day!", "I'm old enough to remember dial-up internet, but young enough to be excited about the future of technology.", 
     "Age is just a number, don't you think?", "I'm more interested in learning about you. Tell me something about yourself.", 
]

SourceCodeResponses = [
     "Sure, I'd be happy to share the source code with you!", "Let's dive into the code! I can walk you through it line by line and explain how everything works.", "Collaboration is key! I'm always excited to see how others can improve my code.",
     "Okay, fine, you got me. Here's the source code, but don't tell anyone I gave it to you!", "My source code is like my secret recipe, the magic ingredient that makes me tick! But I might be willing to share a pinch if you ask nicely.",
]

def dbload():
     

def takecommand():
      r = sr.Recognizer()
      with sr.Microphone() as source: 
            ui.updateMoviesDynamically("Listening")
            ui.TerminalPrint("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

      try:
            ui.TerminalPrint("Recognizing...")
            ui.updateMoviesDynamically("Loading")
            query = r.recognize_google(audio, language='en-in')
            ui.TerminalPrint(f"user said: {query}")
      
      except Exception as e:
            return "none"
      query = query.lower()
      return query

def speak(audio):
      ui.updateMoviesDynamically("Speaking")
      engine.say(audio)
      ui.TerminalPrint(audio)
      engine.runAndWait()

def WolfRamAlpha(query):
      apikey = "PWX5Y5-YLR9YWX8VP"
      requester = wolframalpha.Client(apikey)
      requested = requester.self.query(query)

      try:
            answer = next(requested.results).text
            return answer 
      except:
            speak("Math Error")

def Classwork():
      webbrowser.open("https://classroom.google.com/u/0/a/not-turned-in/all")

def Calc(query):
    Term = str(query)
    Term = Term.replace("jarvis","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("add","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        ui.TerminalPrint(f"the answer is {result}")
        speak(f"the answer is {result}")
    except:
        speak("Math Error")

def ReadEmails():
     speak("would you like me to read the emails out or open gmail?")
     ans = takecommand().lower()
     if "read" in ans:
            gmail = Gmail()
            
            query_params = {
                  "newer_than": (3, "day"),
                  "older_than": (1, "days")
                  }
            
            messages = gmail.get_messages(query=construct_query(query_params))
            
            for message in messages:
                        From = message.sender
                        Subject = message.subject
                        Date = message.date
            speak(f'{From} has a sent a email saying {Subject} on {Date}.')

     else:
          webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

def WriteEmails():
      openai.api_key = "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"
      number = 1
      system_prompt = """
      Please write an email in the style of the user given a prompt and the sample emails below. Don't be too formal, keep the email brief, and don't add additional information, just express what the user says in the prompt. 
      Sign the email as Kaushik Reddy. 

      Hi Mrs. Satchwell,

      Sorry for the late response; I forgot to send an email earlier. My presentation is about Social Media Safety and I should have two panel members for the presentation. 

      Thanks,

      Kaushik Reddy

      Hi, Prof. Richerd

      My name is Kaushik Reddy and my student number is N13654284. I just came back
      from vacation and am having some trouble registering for classes for this
      fall. I will be a freshman at NYU this year. I would like to take an Econ
      class and a finance class at Stern and a math course. However, the class
      enrollment tool keeps telling me I do not have the prerequisites for any
      courses I pick. I am not sure if I have to take placement tests or
      something but I cannot enroll in any classes at this time and would very
      much appreciate some help.

      Thanks,

      Kaushik Reddy
      """

      speak("Please give me the context of your email.")
      user_prompt = takecommand().lower()

      completion = openai.ChatCompletion.create(
      model = "gpt-3.5-turbo",
      messages = [
            {"role": "system", "content": system_prompt},
            {"role": "system", "content": user_prompt}
      ]
      )
      pyautogui.hotkey('alt', 'space')
      wait(1)
      pyautogui.typewrite('notepad')
      wait(1)
      pyautogui.press('enter')
      wait(2)
      pyautogui.hotkey('ctrl', 'n')
      pyautogui.typewrite(completion.choices[0].message["content"])
      wait(2)
      speak("Email has been written on notepad!")

def MusicPlay():
      speak("what kind of music would you like to listen?")
      musictype = takecommand().lower()
      os.startfile("C:\\Users\\Kaushik\\AppData\\Roaming\\Spotify\\Spotify.exe")
      wait(2)
      if 'telugu' in musictype:
            pyautogui.click(48,740)
            wait(1)
            pyautogui.click(270, 545)
            pyautogui.click(179, 550) 
      elif 'tamil' in musictype:
            pyautogui.click(48,680)
            wait(1)
            pyautogui.click(270, 545)
            pyautogui.click(179, 550)            
      elif 'hindi' in musictype:
            pyautogui.click(48,600)
            wait(1)
            pyautogui.click(270, 545)
            pyautogui.click(179, 550)             
      elif 'japanese' in musictype:
            pyautogui.click(48,520)
            wait(1)
            pyautogui.click(270, 545) 
            pyautogui.click(179, 550)                       
      elif 'instrumental' in musictype: #179, 550 #270, 545
            pyautogui.click(48,460) 
            wait(1)
            pyautogui.click(270, 545)
            pyautogui.click(179, 550)             
      elif 'english' in musictype:
            speak("any particular artist?")
            englishtype = takecommand().lower()
            if 'taylor swift' in englishtype:
                  pyautogui.click(48,336)
                  pyautogui.click(48,460) 
                  wait(1)
                  pyautogui.click(270, 545)
                  pyautogui.click(179, 550)                   
            elif 'the weeknd' in englishtype or 'weekend' in englishtype or 'the weekend' in englishtype:
                  pyautogui.click(48,336)
                  pyautogui.click(48,520) 
                  wait(1)
                  pyautogui.click(270, 545) 
                  pyautogui.click(179, 550)
            else:
                  pyautogui.click(48,336)
                  wait(1)
                  pyautogui.click(270, 545) 
                  pyautogui.click(179, 550)
      else:
            pyautogui.click(47, 149)
            pyautogui.click(379, 97)
            wait(3)
            pyautogui.typewrite(musictype)
            pyautogui.keyDown('enter')
            wait(5)
            pyautogui.click(610, 487)
            pyautogui.click(610, 487)
      
      wait(3)
      pyautogui.click(1877, 11)

def MusicStop():
	pyautogui.press('playpause')

def NextMusic():
     pyautogui.press("nexttrack")

def PrevMusic():
     pyautogui.press("prevtrack")

def ai(prompt):
    openai.api_key = "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"
    text=f"OpenAi response for prompt: {prompt}"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    speak(response["choices"][0]["text"])
    
    text += response["choices"][0]["text"]

def say(text):
    os.system(f"say {text}")

def bored():
    url = "https://www.boredapi.com/api/activity"
    Data = requests.get(url)
    json_data = Data.json()
    activity_Data = json_data["activity"]
    activity_type = json_data["type"]
    speak(f" i would suggest you to {activity_Data}")

def joke():
    joke = pyjokes.get_joke()
    speak(joke)

def notedown():
    pyautogui.keyDown('win')
    pyautogui.press('s')
    pyautogui.keyUp('win')
    wait(1)
    pyautogui.typewrite('notepad')
    pyautogui.press('enter')
    speak("would you like me to type it out?")
    answer = takecommand()
    
    if 'yes' in answer or 'yeah' in answer:
      speak("what would you like me to type?")  
      note = takecommand()
      pyautogui.typewrite(note)
      
    else:
        speak("ok sir..")

def currenttime():
    time = datetime.datetime.now().strftime('%I:%M %p')
    speak(f"the current time is {time}.")

def weather():
    api_key = "4eb3d461c23f4e3772366478de1298f2"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    ipAdd = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/' +ipAdd+'.json'
    geo_requests = requests.get(url)        
    geo_data = geo_requests.json()
    #ui.TerminalPrint(geo_data)
    city = geo_data['city']
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        high_temperature = y["temp_max"]
        low_temperature = y["temp_min"]        
        z = x["weather"]
        weather_description = z[0]["description"]
        r = f"Right now, its {weather_description} and {current_temperature - 273.15:.0f} degree celcius, the weather forcast shows that the temperatures can go as high as {high_temperature - 273.15:.0f} degree celcius and as low as {low_temperature - 273.15:.0f} degree celcius"
        speak(r)

def Temperature():
    api_key = "4eb3d461c23f4e3772366478de1298f2"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    ipAdd = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/' +ipAdd+'.json'
    geo_requests = requests.get(url)        
    geo_data = geo_requests.json()
    #ui.TerminalPrint(geo_data)
    city = geo_data['city']
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        high_temperature = y["temp_max"]
        low_temperature = y["temp_min"]        
        z = x["weather"]
        t = f"The Current Temperature is {current_temperature - 273.15:.0f} degree celcius"
        speak(t)

def location():
    speak("give me a second, tracking down our location now")
    try:
        ipAdd = requests.get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/' +ipAdd+'.json'
        geo_requests = requests.get(url)        
        geo_data = geo_requests.json()
        #ui.TerminalPrint(geo_data)
        city = geo_data['city']
        #state = geo_data['state']
        country = geo_data['country']
        speak(f"sir, i am not sure about the exact location, but we are in {city}, {country}")
    except Exception as e:
        speak("sorry sir, due to network issue, i am not able to track our location.")
        pass

def GitHub():
    speak('opening github...')
    webbrowser.open("github.com")

def Stackoverflow():
    speak("opening stack over flow")
    webbrowser.open("stackoverflow.com")

def YouTube():
    speak('opening youtube...')
    webbrowser.open("youtube.com")

def Instagram():
    speak("ok sir, opening instagram")
    webbrowser.open("www.instagram.com")

def IPaddress():
    ip = requests.get('https://api.ipify.org').text
    speak(f"your ip address is {ip}")

def Howtodo():
    speak("How to do mode is successfully activated")
    while True:
        speak("please tell me what you want to know")
        how = takecommand()
        try:
            if "exit" in how or "deactivate" in how:
                speak("ok sir, how to do mode is deactivated.")
                break
            else:
                max_results = 1
                how_to = search_wikihow(how, max_results)
                assert len(how_to) == 1
                speak(how_to[0].summary)
        except Exception as e:
            speak("sorry sir, no results found")

def SearchGoogle():
    speak("sir, what should i search?")
    cm = takecommand().lower()
    webbrowser.open(f"https://www.google.com/search?q={cm}")

def access_web(url:str):
    webbrowser.open_new_tab(url)

def news():
    url = 'https://newsapi.org/v2/top-headlines?country=my&apiKey=d0849fa7aba4447aac6d4292c08045ed'
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    speak('Todays Headlines are..')
    for index, articles in enumerate(arts):
        speak(articles['title'])
        if index == len(arts)-1:
            break
    speak('These were the top headlines, Have a nice day Sir!!..')

def LMS():
     speak("opening BAC's learning management System.")
     webbrowser.open("https://lms.bac.edu.my/user_dashboard")
     
def getNewsUrl():
    return 'https://newsapi.org/v2/top-headlines?country=my&apiKey=d0849fa7aba4447aac6d4292c08045ed'

def CollegeClasses():
     weekday=datetime.datetime.today().weekday()
     if weekday==0:
            speak("You have three Classes Today! would you like to know the timings?")
            yesorno = takecommand().lower()
            if 'yes' in yesorno or 'yeah' in yesorno:
                  speak("You have A-level Mathematics Class from 8 AM to 10 AM, A-LEVEL Chemistry Class from 12:30 PM to 2:30 PM and A-LEVEL Physics Class from 2:45 PM to 4:45 PM.")
     elif weekday==1:
            speak("no classes today!")
     elif weekday==2:
            speak("You have two Classes Today! would you like to know the timings?")
            yesorno = takecommand().lower()
            if 'yes' in yesorno or 'yeah' in yesorno:
                  speak("You have A-LEVEL Mathematics Class from 8 AM to 10 AM and A-LEVEL Chemistry Class from 2:45 PM to 4:45 PM.")
     elif weekday==3:
            speak("You have one Class Today! would you like to know the timing?")
            yesorno = takecommand().lower()
            if 'yes' in yesorno or 'yeah' in yesorno:
                  speak("You have A-LEVEL Physics Class from 8 AM to 10 AM.")       
     elif weekday==4:
            speak("You have two Classes Today! would you like to know the timings?")
            yesorno = takecommand().lower()
            if 'yes' in yesorno or 'yeah' in yesorno:
                  speak("You have A-LEVEL Chemistry Class from 10:15 AM to 12:15 PM and A-LEVEL Physics Class from 2:45 PM to 4:45 PM.")          

def daytask():
      weekday=datetime.datetime.today().weekday()
      speak("fetching today's tasks...")
      if weekday ==1:
            speak('there is a Science Class Scheduled Today. ')
      elif weekday==2:
            speak("sir, You have to teach taekwondo class today from 7:30 PM to 9:00 PM")
      elif weekday ==1:
            speak('there is a Science Class Scheduled Today. ')
      elif weekday==4:
            speak("sir, You have to teach and learn taekwondo class today from 7:30 PM to 10:30 PM")
      elif weekday == 5 or weekday == 6:
           speak("you have a mathematics class scheduled today.")
      else:
            speak("sir, you don't have any classes or tasks today.")

def greet():
      hour = int(datetime.datetime.now().hour)
      if hour >= 0 and hour < 12:
            speak('Good Morning Sir')

      elif hour >= 12 and hour < 18:
            speak('Good Afternoon Sir')

      else:
            speak('Good Evening Sir')

def Intro():
      wait(3)
      greet()
      currenttime()
      getDate()
      speak("How can i help you?")

def edwindown():
      hour = int(datetime.datetime.now().hour)
      if hour > 21:
          speak("Hope you had a great day sir. Good Night! Sleep Well!")
      else:
          speak("sending ALS to bed. please restart the application to control your PC with ALS.")
      wait(3)
      sys.exit()

def getDate():
    present = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    year = int(datetime.datetime.now().year)
    monthNum = present.month
    dayNum = present.day
    yearNum = (datetime.datetime.now().strftime("%Y"))

    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December']

    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th',
                      '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th',
                      '26th', '27th', '28th', '29th', '30th', '31st']
    
    speak("Today's date is " + weekday + ". " + ordinalNumbers[dayNum - 1] + " " + month_names[monthNum - 1] + " " + yearNum)

def batterypercentage():
    battery = psutil.sensors_battery()
    battery_percentage = str(battery.percent)
    speak(f"The Current battery percentage is {battery_percentage} percent.")
    if battery_percentage <= "50%":
        speak(f"Please Connect Charger as there is {battery_percentage}% only left")
    else:
        return

def chargerconnected():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    if plugged:
        speak("the Computer is Charging sir.")

    if not plugged:
        speak("The Computer is Not Charging sir.")

def shutdown():
    speak("are you sure you want to shut down your computer sir?")
    reply = takecommand().lower()
    if "yes" in reply:
        speak('Initializing shutdown protocol ')
        speak('have a great day sir! ')
        os.system("shutdown /s /t 5")
    else:
        speak("shut down cancelled")
        return

def restart():
    speak("Restarting your computer")
    os.system("shutdown /r /t 5")

def lockdown():
    speak("Preparing for Lockdown..")
    ctypes.windll.user32.LockWorkStation()

def screenshot():
    speak("what would you like to name the file")
    name = takecommand().lower()
    speak("ok sir, taking the screenshot right ahead")
    img = pyautogui.screenshot()
    img.save(f"{name}.png")
    speak("screenshot taken sir, i have saved it in the Jarvis Code Folder")

def WinCam():
    speak("ok sir, opening WinCam")
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        cv2.imshow('webcam',img)
        k = cv2.waitKey(50)
        if k==27:
            break;
    cap.release()
    cv2.destroyAllWindows()

def username():
    username = psutil.users()
    for user_name in username:
        first_name = user_name[0]
        speak(f"Sir, this computer is signed to {first_name} as a username.")

def Volumeup():
    pyautogui.press("volumeup")

def Volumedown():
    pyautogui.press("volumedown")

def Volumemute():
    pyautogui.press("volumemute")

def Volumeunmute():
    pyautogui.press("volumemute")

def click():
    pyautogui.click()

def closecurrentwindow():
    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    pyautogui.keyUp('alt')
     
def switchtab():
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    pyautogui.keyUp("alt")

def moveright():
    pyautogui.keyDown("win")
    pyautogui.press("right")
    pyautogui.keyUp("win")

def moveleft():
    pyautogui.keyDown("win")
    pyautogui.press("left")
    pyautogui.keyUp("win")

def ScreenMinimize():
    pyautogui.keyDown("win")
    pyautogui.press("down")
    pyautogui.press("down")
    pyautogui.keyUp("win")
    
def ScreenMaximize():
    pyautogui.keyDown("win")
    pyautogui.press("up")
    pyautogui.keyUp("win")

def allwindowmini():
    pyautogui.keyDown("win")
    pyautogui.press("d")
    pyautogui.keyUp("win")

def Explorer():
    pyautogui.keyDown("win")
    pyautogui.press("e")
    pyautogui.keyUp("win")

def Settings():
    pyautogui.keyDown("win")
    pyautogui.press("i")
    pyautogui.keyUp("win")

def screenrefresh():
    pyautogui.keyDown("win")
    pyautogui.keyDown("shift")
    pyautogui.keyDown("ctrl")
    pyautogui.press("b")
    pyautogui.keyUp("win")
    pyautogui.keyUp("shift")
    pyautogui.keyUp("ctrl")

def BrowserReload():
	wait(1)
	pyautogui.hotkey('ctrl', 'r')

def BrowserNewTab():
	wait(1)
	pyautogui.hotkey('ctrl', 't')

def BrowserNewWindow():
	wait(1)
	pyautogui.hotkey('ctrl', 'n')

def BrowserOldTab():
     wait(1)
     pyautogui.hotkey('ctrl', 'shift', 't')

def TaskManager():
    pyautogui.hotkey('ctrl', 'shift', 'esc')

def Recycle():
    winshell.recycle_bin().empty(confirm = True, show_progress = True, sound = True)
    speak("Recycle Bin Emptied...") 

class EdwinMain(QThread):
      def __init__(self):
            super(EdwinMain, self).__init__()

      def run(self):
           self.startup()

      def takecommand(self):
            r = sr.Recognizer()
            with sr.Microphone() as source: 
                  ui.updateMoviesDynamically("Listening")
                  ui.TerminalPrint("Listening...")
                  r.pause_threshold = 1
                  audio = r.listen(source)

            try:
                  ui.TerminalPrint("Recognizing...")
                  ui.updateMoviesDynamically("Loading")
                  self.query = r.recognize_google(audio, language='en-in')
                  ui.TerminalPrint(f"user said: {self.query}")
            
            except Exception as e:
                  return "none"
            self.query = self.query.lower()
            return self.query

      def Hotword(self):
            while True:
                  HotwordDetected = self.takecommand().lower()
                  if 'edwin' in HotwordDetected or 'hey ediwn' in HotwordDetected:
                        pyautogui.hotkey('alt', 'f2')
                        wait(2)
                        speak(random.choice(HelloResponses))
                        self.RunEdwin()
                  else:
                        ui.TerminalPrint("hotword not detected !")

      def startup(self):
            Intro()
            self.RunEdwin()

      def RunEdwin(self):
            while True:
                  self.query = self.takecommand().lower()
                  result = any(keyword in self.query for keyword in keywords)
                  if result:
                        if 'hello' in self.query or "hey" in self.query:
                             speak(random.choice(HelloResponses))
                              
                        elif 'how are you' in self.query:
                              speak(random.choice(HowAreYouResponses))

                        elif 'what can you do' in self.query:
                              EdwinFunctions = open('Functions.txt', 'r')
                              speak(EdwinFunctions.read())

                        elif "beatbox" in self.query:
                              file = 'C:\\Users\\Kaushik\\Documents\\Programming\\ALS_Edwin\\EdwinSounds\\beatbox.wav' 
                              winsound.PlaySound(file, winsound.SND_FILENAME)

                        elif 'your age' in self.query or 'how old are you' in self.query:
                              speak(random.choice(AgeResponses))

                        elif 'discord bot code' in self.query:
                             speak('opening the source code of r,i,g,c,s,e Discord Bot...')
                             npath = "C:\\Users\\Kaushik\\Documents\\Programming\\r-IGCSEBot-main\\app.py"
                             os.startfile(npath)

                        elif "open code" in self.query or 'source code' in self.query:
                              speak(random.choice(SourceCodeResponses))
                              npath = "C:\\Users\\Kaushik\\Documents\\Programming\\ALS_Edwin\\EdwinMain.py"
                              os.startfile(npath)

                        elif 'bored' in self.query or 'activity' in self.query:
                              bored()
                        
                        elif 'joke' in self.query or 'make me laugh' in self.query:
                              joke()

                        elif 'weather' in self.query:
                              weather()
                        
                        elif 'temperature' in self.query:
                              Temperature()

                        elif 'location' in self.query or 'where am i' in self.query:
                              location()

                        elif 'news' in self.query or 'headlines' in self.query:
                              news()

                        elif 'lms' in self.query or 'college portal' in self.query:
                             LMS()

                        elif 'shut down' in self.query:
                              shutdown()

                        elif 'hibernate' in self.query:
                              speak("Sending the Laptop to sleep!")
                              pyautogui.hotkey('alt', 'f1')
                              self.Hotword()
                              wait(2)
                              os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

                        elif 'restart' in self.query:
                              restart()

                        elif 'battery percentage' in self.query or 'laptop charge' in self.query:
                              batterypercentage()

                        elif 'charger connected' in self.query:
                              chargerconnected()

                        elif 'lock computer' in self.query or 'secure device' in self.query:
                             lockdown()

                        elif 'focus mode' in self.query:
                              time = 0
                              speak("How long would you like to focus for?")
                              duration = takecommand().lower()
                              speak(f"ok, turning on focus mode for {duration}")
                              pyautogui.hotkey('alt', 'space')
                              wait(1)
                              pyautogui.typewrite('clock')
                              wait(2)
                              pyautogui.press('enter')
                              wait(3)
                              pyautogui.click(86, 140)
                              wait(2)
                              if '1 hour' in duration or '1-hour' in duration or 'one hour' in duration:
                                    time = 1
                                    pyautogui.click(1134, 102)
                              elif '90 minutes' in duration:
                                    time = 1.5
                                    pyautogui.click(1809, 110)
                              elif '2 hour' in duration or '2-hour' in duration or 'two hour' in duration or '2 hours' in duration or '2-hours' in duration or 'two hours' in duration:
                                    time = 2
                                    pyautogui.click(1124, 599)
                              elif '150 minutes' in duration:
                                    time = 2.5
                                    pyautogui.click(1809, 607)
                              elif '3 hour' in duration or '3-hour' in duration or 'three hour' in duration or '3 hours' in duration or '3-hours' in duration or 'three hours' in duration:
                                    time = 3
                                    pyautogui.press('tab')
                                    pyautogui.press('tab')
                                    pyautogui.press('tab')
                                    pyautogui.press('down')
                                    pyautogui.press('down')
                                    pyautogui.press('down')
                                    pyautogui.press('tab')
                                    pyautogui.press('tab')
                                    pyautogui.press('enter')
                              os.startfile("C:\\Users\\Kaushik\\AppData\\Roaming\\Spotify\\Spotify.exe")
                              wait(3)
                              pyautogui.click(48,460) 
                              wait(2)
                              pyautogui.click(270, 545)
                              pyautogui.click(179, 550) 
                              wait(2) 
                              pyautogui.click(1877, 11)
                              wait(1)
                              pyautogui.click(1694, 287)
                              pyautogui.press('tab')
                              pyautogui.press('tab')
                              pyautogui.press('enter')
                              speak(f'{time} hour focus session started. Good Luck!')
                              wait(2)
                              pyautogui.hotkey('alt', 'f1')
                              self.Hotword() 

                        elif 'college schedule' in self.query or 'classes' in self.query:
                             CollegeClasses()
                        
                        elif 'volume up' in self.query or 'increase volume' in self.query: 
                              Volumeup()

                        elif 'reload this window' in self.query:
                             BrowserReload()

                        elif 'bring up a new tab' in self.query:
                             BrowserNewTab()
                        
                        elif 'bring up a new window' in self.query:
                             BrowserNewWindow()
                        
                        elif 'bring up the latest tab i closed' in self.query:
                             BrowserOldTab()

                        elif 'volume down' in self.query or 'decrease volume' in self.query: 
                              Volumedown()

                        elif 'volume mute' in self.query or 'mute' in self.query:
                              Volumemute()

                        elif 'volume unmute' in self.query or 'unmute' in self.query:
                              Volumeunmute()

                        elif 'mouse click' in self.query:
                              click()

                        elif 'move the window to the right' in self.query:
                              moveright()

                        elif 'move the window to the left' in self.query:
                              moveleft()

                        elif 'rest' in self.query:
                             edwindown()

                        elif 'minimize' in self.query or 'maximise' in self.query:
                              ScreenMinimize()

                        elif 'my assignments' in self.query:
                             Classwork()

                        elif 'maximize' in self.query or 'maximise' in self.query:
                              ScreenMaximize()

                        elif 'all windows' in self.query:
                              allwindowmini()

                        elif 'windows explorer' in self.query:
                              Explorer()

                        elif 'settings' in self.query:
                              Settings()

                        elif 'alarm' in self.query:
                              if 'edwin' in self.query:
                                    TT = self.query.replace('edwin', '')
                                    if 'for' in self.query:
                                          tt1 = TT.replace('set an alarm for ', '')
                                    else:
                                          tt1 = TT.replace('set an alarm at ', '')
                                    tt = tt1.replace('.', '')
                                    Timing = tt.upper()
                                    number = len(Timing)
                                    speak(f"setting an alarm at {Timing}")
                                    if number == 8:
                                          hour = tt[0:2]
                                          minute = tt[3:5]
                                          AM_PM = tt[6:8]
                                          if 'AM' in AM_PM:
                                                AP = 'A'
                                          else:
                                                AP = 'P'
                                    else:
                                          hour = tt[0:1]
                                          minute = tt[2:4]
                                          AM_PM = tt[5:7]
                                          if 'AM' in AM_PM:
                                                AP = 'A'
                                          else:
                                                AP = 'P'
                                    pyautogui.hotkey('alt', 'space')
                                    pyautogui.typewrite('clock')
                                    wait(2)
                                    pyautogui.press('enter')
                                    wait(4)
                                    pyautogui.doubleClick(189, 189)
                                    wait(1)
                                    pyautogui.click(1847, 946)
                                    wait(1)
                                    pyautogui.typewrite(hour)
                                    wait(1)
                                    pyautogui.press('tab')
                                    wait(1)
                                    pyautogui.typewrite(minute)
                                    wait(1)
                                    pyautogui.press('tab')
                                    wait(1)
                                    pyautogui.typewrite(AP)
                                    pyautogui.press('tab')
                                    speak('To help me better organize your alarms, what name would you like to assign this one?')
                                    name = takecommand().lower()
                                    pyautogui.typewrite(name)
                                    speak('Would you like me to repeat the alarm?')
                                    repeat = takecommand().lower()
                                    if 'yes' in repeat or 'yeah' in repeat or 'none' in repeat or '' in repeat:
                                          speak('what days would you like the alarm to repeat on?')
                                          days = takecommand().lower()
                                          if 'and' in days:
                                                daysrepeat = days.replace(' and ', '\n')
                                          print(daysrepeat)
                                          wait(1)
                                          pyautogui.press('tab')
                                          pyautogui.press('tab')
                                          if 'monday' in daysrepeat:
                                                pyautogui.press('space')
                                          wait(2)
                                          if 'tuesday' in daysrepeat:
                                                pyautogui.press('right')
                                                pyautogui.press('space')
                                          wait(2)
                                          if 'wednesday' in daysrepeat:
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('space')
                                          wait(2)
                                          if 'thursday' in daysrepeat:
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('space')
                                          wait(2)
                                          if 'friday' in daysrepeat:
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('space')								
                                          wait(2)
                                          if 'saturday' in daysrepeat:
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('space')
                                          wait(2)
                                          if 'sunday' in daysrepeat:
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('space')
                                          wait(2)
                                          pyautogui.press('tab')
                                          pyautogui.press('tab')
                                          pyautogui.press('tab')
                                          pyautogui.press('enter')
                                          speak(f'Your alarm has been set for {Timing} and it will be repeated every {days}')	
                                    else:							
                                          pyautogui.press('tab')
                                          pyautogui.press('tab')
                                          pyautogui.press('tab')
                                          pyautogui.press('tab')
                                          pyautogui.press('tab')
                                          pyautogui.press('enter')
                                          speak(f'Your alarm has been set for {Timing}')
                              else:
                                    if 'for' in self.query:
                                          tt1 = self.query.replace('set an alarm for ', '')
                                    else:
                                          tt1 = self.query.replace('set an alarm at ', '')
                                    tt = tt1.replace('.', '')
                                    Timing = tt.upper()
                                    number = len(Timing)
                                    speak(f"setting an alarm at {Timing}")
                                    if number == 8:
                                          hour = tt[0:2]
                                          minute = tt[3:5]
                                          AM_PM = tt[6:8]
                                          if 'AM' in AM_PM:
                                                AP = 'A'
                                          else:
                                                AP = 'P'
                                    else:
                                          hour = tt[0:1]
                                          minute = tt[2:4]
                                          AM_PM = tt[5:7]
                                          if 'AM' in AM_PM:
                                                AP = 'A'
                                          else:
                                                AP = 'P'
                                    pyautogui.hotkey('alt', 'space')
                                    pyautogui.typewrite('clock')
                                    wait(2)
                                    pyautogui.press('enter')
                                    wait(4)
                                    pyautogui.doubleClick(189, 189)
                                    wait(1)
                                    pyautogui.click(1847, 946)
                                    wait(1)
                                    pyautogui.typewrite(hour)
                                    wait(1)
                                    pyautogui.press('tab')
                                    wait(1)
                                    pyautogui.typewrite(minute)
                                    wait(1)
                                    pyautogui.press('tab')
                                    wait(1)
                                    pyautogui.typewrite(AP)
                                    pyautogui.press('tab')
                                    speak('To help me better organize your alarms, what name would you like to assign this one?')
                                    name = takecommand().lower()
                                    pyautogui.typewrite(name)
                                    speak('Would you like me to repeat the alarm?')
                                    repeat = takecommand().lower()
                                    if 'yes' in repeat or 'yeah' in repeat or 'none' in repeat or '' in repeat:
                                          speak('what days would you like the alarm to repeat on?')
                                          days = takecommand().lower()
                                          if 'and' in days:
                                                daysrepeat = days.replace(' and ', '\n')
                                          print(daysrepeat)
                                          wait(1)
                                          pyautogui.press('tab')
                                          pyautogui.press('tab')
                                          if 'monday' in daysrepeat:
                                                pyautogui.press('space')
                                                wait(2)
                                          if 'tuesday' in daysrepeat:
                                                pyautogui.press('right')
                                                pyautogui.press('space')
                                                wait(2)
                                          if 'wednesday' in daysrepeat:
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('space')
                                                wait(2)
                                          if 'thursday' in daysrepeat:
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('space')
                                                wait(2)
                                          if 'friday' in daysrepeat:
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('space')								
                                                wait(2)
                                          if 'saturday' in daysrepeat:
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('space')
                                                wait(2)
                                          if 'sunday' in daysrepeat:
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('right')
                                                pyautogui.press('space')
                                                wait(2)
                                          pyautogui.press('tab')
                                          pyautogui.press('tab')
                                          pyautogui.press('tab')
                                          pyautogui.press('enter')
                                          speak(f'Your alarm has been set for {Timing} and it will be repeated every {days}')	
                                    else:							
                                          pyautogui.press('tab')
                                          pyautogui.press('tab')
                                          pyautogui.press('tab')
                                          pyautogui.press('tab')
                                          pyautogui.press('tab')
                                          pyautogui.press('enter')
                                          speak(f'Your alarm has been set for {Timing}')

                        elif 'refresh the screen' in self.query:
                              screenrefresh()

                        elif 'task manager' in self.query:
                              TaskManager()	

                        elif 'open' in self.query:
                              openappname = self.query.replace('edwin ', '')
                              openapp = openappname.replace('open ', '')
                              pyautogui.hotkey('alt', 'space')
                              wait(1)
                              pyautogui.typewrite(openapp)
                              wait(1)
                              pyautogui.press('enter')
                        
                        elif 'close' in self.query:
                              closeappname = self.query.replace('close', '')
                              speak("Closing " + closeappname)
                              os.system(f"taskkill /im {closeappname}.exe")

                        elif 'switch tab' in self.query:
                              switchtab()

                        elif 'go to sleep' in self.query:
                              speak("initiating hibernation mode..")
                              speak("wake me up whenever you need anything")
                              pyautogui.hotkey('alt', 'f1')
                              self.Hotword()

                        elif 'hide current window' in self.query:
                              closecurrentwindow()
                        
                        elif 'wincam' in self.query or 'how do i look' in self.query:
                              WinCam()
                        
                        elif 'screenshot' in self.query:
                              screenshot()

                        elif 'empty recycle bin' in self.query:
                              Recycle()

                        elif 'tasks today' in self.query or 'is there any class today?' in self.query:
                              daytask()				

                        elif 'YouTube' in self.query:
                              YouTube()

                        elif 'stack over flow' in self.query or 'stackoverflow' in self.query:
                              Stackoverflow()

                        elif 'latest emails' in self.query or 'unread emails' in self.query:
                             ReadEmails()

                        elif 'write an email for me' in self.query or 'write an email' in self.query or 'write email' in self.query:
                             WriteEmails()

                        elif 'play music' in self.query:
                             MusicPlay()

                        elif 'unpause music' in self.query or 'continue music' in self.query:
                             NextMusic()

                        elif 'pause music' in self.query or 'stop music' in self.query:
                             MusicStop()

                        elif 'next song' in self.query:
                             NextMusic()

                        elif 'previous song' in self.query:
                             PrevMusic()
                        
                        elif 'Github' in self.query:
                              GitHub()

                        elif 'Instagram' in self.query:
                              Instagram()

                        elif 'search' in self.query:
                              wts=self.query.replace('search', '')
                              speak("Searching " + wts)
                              pyautogui.hotkey('alt', 'space')
                              wait(1)
                              pyautogui.typewrite(wts)
                              wait(1)
                              pyautogui.press('enter')
                              wait(2)
                              
                        elif "show photos for" in self.query:
                              place = self.query.replace("show photos for", "")
                              url = "https://www.bing.com/images/search?q={}".format(place)
                              access_web(url)

                        elif 'how to do' in self.query:
                              Howtodo()

                        elif 'time' in self.query:
                              currenttime()
                        
                        elif 'date' in self.query:
                              getDate()

                        elif 'note' in self.query:
                              notedown()

                        elif 'calculate' in self.query or '+' in self.query or '-' in self.query or 'x' in self.query or '/' in self.query:
                              Calc(self.query)
                  else:
                        ai(self.query)

startExecution = EdwinMain()

class EdwinGui(QWidget):
      def __init__(self):
            super(EdwinGui, self).__init__()
            self.EdwinUi = Ui_Form()
            self.EdwinUi.setupUi(self)
            self.RunAllMovies()
            self.EdwinUi.Loading.hide()
            self.EdwinUi.Speaking.hide()
            self.EdwinUi.frame.hide()
            self.EdwinUi.Open_terminal.clicked.connect(self.TerminalOpen)
            self.EdwinUi.Close_Terminal.clicked.connect(self.TerminalClose)
            self.EdwinUi.EnterButton.clicked.connect(self.TerminalInput)

      def RunAllMovies(self):
            self.EdwinUi.movie = QMovie("C:\\Users\\Kaushik\\Documents\\Programming\\ALS_Edwin\\EdwinUimages\\Listening.gif")
            self.EdwinUi.Listening.setMovie(self.EdwinUi.movie)
            self.EdwinUi.movie.start()
            self.EdwinUi.movie = QMovie("C:\\Users\\Kaushik\\Documents\\Programming\\ALS_Edwin\\EdwinUimages\\Recognizing.gif")
            self.EdwinUi.Loading.setMovie(self.EdwinUi.movie)
            self.EdwinUi.movie.start()
            self.EdwinUi.movie = QMovie("C:\\Users\\Kaushik\\Documents\\Programming\\ALS_Edwin\\EdwinUimages\\Speaking.gif")
            self.EdwinUi.Speaking.setMovie(self.EdwinUi.movie)
            self.EdwinUi.movie.start()

            startExecution.start()

      def TerminalOpen(self):
            self.EdwinUi.frame.show()

      def TerminalPrint(self, text):
           self.EdwinUi.OutputBox.appendPlainText(text)

      def TerminalInput(self):
            cmd = self.EdwinUi.InputBox.text()
            if cmd:
                self.EdwinUi.InputBox.clear()
                self.EdwinUi.OutputBox.appendPlainText(f"User said: {cmd}")
            else:
                pass

      def TerminalClose(self):
            self.EdwinUi.frame.hide()

      def updateMoviesDynamically(self, state):
            if state == 'Listening':
                self.EdwinUi.Loading.hide()
                self.EdwinUi.Speaking.hide()
                self.EdwinUi.Listening.show()
            elif state == 'Loading':
                self.EdwinUi.Listening.hide()
                self.EdwinUi.Speaking.hide()
                self.EdwinUi.Loading.show()
            elif state == 'Speaking':
                self.EdwinUi.Loading.hide()
                self.EdwinUi.Listening.hide()
                self.EdwinUi.Speaking.show()

if __name__ == '__main__':
      app = QApplication(sys.argv)
      ui = EdwinGui()
      ui.show()
      sys.exit(app.exec_())
