import pyttsx3
from time import sleep as wait
import pyautogui
import speech_recognition as sr
from Bard import Chatbot

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate",180)

def takecommand():
	r = sr.Recognizer()
	with sr.Microphone() as source: 
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language='en-in')
		print(f"user said: {query}")
	
	except Exception as e:
		return "none"
	query = query.lower()
	return query

def speak(audio):
      engine.say(audio)
      print(audio)
      engine.runAndWait()


import requests
import json
 
# Replace "YOUR_API_KEY" with the actual API Key obtained in Step 1
API_KEY = "AIzaSyCcEwRWLf5rQqVne4SfK5C1IxxvcpZMkKs"
URL = "https://bard.googleapis.com/v1/generate"


def get_bard_response(query):
    response = requests.post(URL, headers=
                   {"Authorization": "Bearer " + API_KEY},
                             json={"query": query})
    data = json.loads(response.content)
    return data["text"]


def main():
    query = "Geeksforgeeks"
    response = get_bard_response(query)
    print("Google Bard Response:")
    print(response)
 
if __name__ == "__main__":
    main()