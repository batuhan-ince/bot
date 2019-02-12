from espeak import espeak
from datetime import datetime
from subprocess import call
import time
import os
def time_now():
    t=datetime.now().strftime("%-d %B %Y %A")
    call(["espeak","-s140","-g10","-ven+f4","The date is %s"%t])
def hello_user():
    call(["espeak","-s180","-ven+f4","Hello! Text to speech activated."])

def xterm():
    os.system("xterm -e \" jackd -d alsa\"&")

def konus(user_text):
    call(["espeak","-s180","-ven+f4",user_text])



