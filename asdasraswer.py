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

seviye = 0
driver = webdriver.Chrome("/home/pi/Desktop/chromedriver")
driver.get("file:///home/pi/Desktop/blockly-games/tr/maze.html")
wait = WebDriverWait(driver,216000)

def emoji_window():
    os.system("xterm -e \"python3 Terminal_style.py\"&")
    time.sleep(25)

for i in range(10):
    wait.until(EC.visibility_of_element_located((By.ID,'dialogDoneText')))
    if driver.find_element_by_id('dialogDoneText').is_displayed() == True:
        concl = driver.find_element_by_xpath('//*[@id="dialogDoneText"]').text[0:1]
        print(concl)
        concl = int(concl)
        seviye = concl-1
       
        if seviye == 3:
            emoji_window()
            
        if seviye == 2:
            ttss.xterm()
            time.sleep(1)
            ttss.hello_user()

        if seviye == 1:
            ttss.konus("You achieved a great deal. Now let's meet. My name is HERMES. What is your Name?")
            tepki = goo.spech()
            tepki1 = tepki.split(" ")
            isim = "Hello " + tepki1[-1]
            ttss.konus(isim)
            

        
    wait.until_not(EC.visibility_of_element_located((By.ID,'dialogDoneText')))
        
        
