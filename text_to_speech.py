from espeak import espeak
from datetime import datetime
from subprocess import call
def time_now():
    t=datetime.now().strftime("%-d %B %Y %A")
    call(["espeak","-s140","-g10","-ven+f4","The date is %s"%t])
def hello_user():
    call(["espeak","-s180","-ven+f4","Hello! Text to speech activated."])

def ayar():
    call(["jack -d alsa"])
    
