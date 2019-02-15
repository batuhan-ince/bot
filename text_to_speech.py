from espeak import espeak
from datetime import datetime
from subprocess import call
from gtts import gTTS
from pygame import mixer
import time
import os
from mutagen.mp3 import MP3
mixer.init()
def time_now():
    t=datetime.now().strftime("%-d %B %Y %A")
    call(["espeak","-s140","-g10","-ven+f4","The date is %s"%t])
def hello_user():
    call(["espeak","-s180","-ven+f4","Hello! Text to speech activated."])

def xterm():
    os.system("xterm -e \" jackd -d alsa\"&")

def konus(user_text):
    call(["espeak","-s180","-ven+f4",user_text])

def konus2(user_text):
    tts = gTTS(user_text, lang='en')
    tts.save("response.mp3")
    mixer.music.load('response.mp3')
    mixer.music.play()
    audioo = MP3("response.mp3")
    pause=audioo.info.length
    time.sleep(pause)
    
