import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime
from datetime import date
import calendar

def chrome(link):
 
    subprocess.call(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
            
    time.sleep(4)
    
    pyautogui.write(link)
    pyautogui.press('enter')
    
    pyautogui.press('enter')
            
    time.sleep(30)
    #while True:
        #audio = pyautogui.locateCenterOnScreen('audioconsent.png')
        #if pyautogui.moveTo(audio) == True:
    pyautogui.press('enter')
            #mute if unmuted
    pyautogui.hotkey('alt','a')
            #break
chrome("www.google.com")
