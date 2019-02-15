#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import subprocess
from asciimatics.screen import Screen
import os
import sys
import text_to_speech as ttss
import googlettsdeneme as goo
import etkilesim as etk

seviye = 0
driver = webdriver.Chrome("/home/pi/Desktop/chromedriver")
driver.get("file:///home/pi/Desktop/blockly-games/tr/maze.html")
wait = WebDriverWait(driver,216000)

def thumbs_up():
    os.system("xterm -e \"python3 thumbs_up.py\"&")
def happy():
    os.system("xterm -e \"python3 happy.py\"&")
def sad():
    os.system("xterm -e \"python3 sad.py\"&")
def hermes_text():
    os.system("xterm -e \"python3 hermes_text.py\"&")
def sad_to_happy():
    os.system("xterm -e \"python3 sad_to_happy.py\"&")
def sound():
    os.system("xterm -e \"python3 sound.py\"&")
    
    
etk.welkam()
for i in range(10):
    wait.until(EC.visibility_of_element_located((By.ID,'dialogDoneText')))
    if driver.find_element_by_id('dialogDoneText').is_displayed() == True:
        concl = driver.find_element_by_xpath('//*[@id="dialogDoneText"]').text[0:2]
        #concl = int(concl)
        seviye = concl
        print(seviye)

        if seviye == '2.':
            happy()
            sad_to_happy()
            sound()
            sad()
            hermes_text()
            thumbs_up()
            
        if seviye == '5.':
            #ttss.xterm()
            #time.sleep(1)
            print("Hello. As you move through your coding adventure I'll have more suprises for you. Let's jump to next chapter")
            ttss.konus2("Hello. As you move through your coding adventure I'll have more suprises for you. Let's jump to next chapter")
                        
        if seviye == '7.':
            print("You achieved a great deal. Now let's meet. My name is HERMES. What is your Name?")
            ttss.konus2("You achieved a great deal. Now let's meet. My name is HERMES. What is your Name?")
            tepki = goo.spech()
            tepki1 = tepki.split(" ")
            isim = "Hello " + tepki1[-1]
            print(isim)
            ttss.konus2(isim)
        
        if seviye == 'Bi':
            print("This demo is over. Please fund my creators to see me in my new gear. Now you can consider me as a personal assistant")
            ttss.konus2("This demo is over. Please fund my creators to see me in my new gear. Now you can consider me as a personal assistant")
            etk.muhabbet()
            
    wait.until_not(EC.visibility_of_element_located((By.ID,'dialogDoneText')))
