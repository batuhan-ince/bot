import random
import datetime
import time
from mutagen.mp3 import MP3
import webbrowser
import text_to_speech as ttss
import wikipedia
from pygame import mixer
import speech_recognition as sr
import pyowm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def muhabbet():
    
    greetings = ['hey there', 'hello', 'hi', 'Hai', 'hey!', 'hey',"ma man"]
    question = ['how are you', 'how are you doing',"what's up","how are you holding up","how you doing"]
    responses = ['Okay', "I'm fine","All is well","I have existential anxiety","same old,same old","I'm hanging in there","Mind your own business"]
    var1 = ['who made you', 'who created you','who designed you']
    var2 = ['I_was_created_by_Team CBILAB_right_in_their_computer.', 'Team CBILAB', 'Allah']
    var3 = ['what time is it', 'what is the time', 'time']
    var4 = ['who are you', 'what is your name','who am i talking to']
    cmd1 = ['open browser', 'open Google',"search"]
    cmd2 = ['play music', 'play songs', 'play a song', 'open music player']
    cmd3 = ['tell a joke', 'tell me a joke', 'say something funny', 'tell something funny']
    jokes = ['Can a kangaroo jump higher than a house? Of course, a house doesn’t jump at all.', 'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.', 'Doctor: Im sorry but you suffer from a terminal illness and have only 10 to live.Patient: What do you mean, 10? 10 what? Months? Weeks?!"Doctor: Nine.']
    cmd4 = ['open YouTube', 'i want to watch a video','YouTube']
    cmd5 = ['tell me the weather', 'weather', 'what about the weather','what is the weather like today','what is the weather like','how is the weather']
    cmd6 = ['exit', 'close', 'goodbye', 'nothing']
    cmd7 = ['what is your color', 'what is your colour', 'your color', 'your color?']
    colrep = ['Right now its rainbow', 'Right now its transparent', 'Right now its non chromatic']
    cmd8 = ['what is your favourite colour', 'what is your favourite color']
    cmd9 = ['thank you']

    repfr9 = ['youre welcome', 'glad i could help you']

    while True:
        now = datetime.datetime.now()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            print("Tell me something:")
            audio = r.listen(source,phrase_time_limit=5)
            try:
                response = r.recognize_google(audio)
                print(response)
                if response in greetings:
                    random_greeting = random.choice(greetings)
                    print(random_greeting)
                    ttss.konus2(random_greeting)
                elif response in question:
                    ttss.konus2('I am fine')
                    print('I am fine')
                elif response in var1:
                    ttss.konus2('I was made by Team CBILAB')
                    reply = random.choice(var2)
                    print(reply)
                elif response in cmd9:
                    print(random.choice(repfr9))
                    ttss.konus2(random.choice(repfr9))
                elif response in cmd7:
                    print(random.choice(colrep))
                    ttss.konus2(random.choice(colrep))
                    print('It keeps changing every micro second')
                    ttss.konus2('It keeps changing every micro second')
                elif response in cmd8:
                    print(random.choice(colrep))
                    ttss.konus2(random.choice(colrep))
                    print('It keeps changing every micro second')
                    ttss.konus2('It keeps changing every micro second')
                elif response in cmd2:
                    mixer.init()
                    mixer.music.load("star_wars.mp3")
                    mixer.music.play()
                    audiio = MP3("star_wars.mp3")
                    pause=audiio.info.length
                    time.sleep(pause+3)
                elif response in var4:
                    ttss.konus2('HERMES')
                elif response in cmd4:
                    driver = webdriver.Chrome("/home/pi/Desktop/chromedriver")
                    driver.get("https://www.youtube.com/watch?v=RLe3wnYN6wA")
                elif response in cmd6:
                    print('see you later')
                    ttss.konus2('see you later')
                    exit()
                elif response in cmd5:
                    owm = pyowm.OWM('2fbe8dc74c321763dfb1406fcab678b1')
                    observation = owm.weather_at_place('Istanbul, TR')
                    observation_list = owm.weather_around_coords(12.972442, 77.580643)
                    w = observation.get_weather()
                    wind=w.get_wind()
                    humidity=w.get_humidity()
                    temperature=w.get_temperature('celsius')
                    print(w)
                    print(w.get_wind())
                    print(w.get_humidity())
                    print(w.get_temperature('celsius'))
                    ttss.konus2('wind speed')
                    ttss.konus2(str(wind['speed']))
                    ttss.konus2('humidity')
                    ttss.konus2(str(humidity) + "percent")
                    ttss.konus2('temperature')
                    ttss.konus2(str(temperature['temp']))
                elif response in var3:

                    print("Current date and time : ")
                    print(now.strftime("The time is %H:%M"))
                    ttss.konus2(now.strftime("The time is %H:%M"))
                elif response in cmd1:
                    driver = webdriver.Chrome("/home/pi/Desktop/chromedriver")
                    driver.get("https://www.google.com")
                elif response in cmd3:
                    jokrep = random.choice(jokes)
                    ttss.konus2(jokrep)
                else:
                    ttss.konus2("please wait")
                    print(wikipedia.summary(response, sentences =1))
                    ttss.konus2(wikipedia.summary(response, sentences = 1))
                
                    
            except sr.UnknownValueError:
                print("Could not understand audio")
                ttss.konus2('I didnt get that. Rerun the code')

def welkam():
    mixer.init()
    mixer.music.load("welcome.mp3")
    mixer.music.set_volume(0.8)
    mixer.music.play()
    audiio = MP3("welcome.mp3")
    pause=audiio.info.length
    time.sleep(pause)
                
                
