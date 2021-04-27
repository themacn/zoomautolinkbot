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


#read schedule
def callloop():
    while True:
                now1 = datetime.now().strftime("%H:%M")
                if now1 in str(df['time']):

                      row = df.loc[df['time'] == now1] 
                      link1 = str(row.iloc[0,1])

                      chrome(link1)
                      time.sleep(40)
                      print("success")

date1 = date.today()
day = calendar.day_name[date1.weekday()]
if day == "Monday":
    df = pd.read_csv('Monday.csv')
    callloop()
if day == "Tuesday":
    df = pd.read_csv('Tuesday.csv')
    callloop()
if day == "Wednesday":
    df = pd.read_csv('Wednesday.csv')
    callloop()
if day == "Thursday":
    df = pd.read_csv('Thursday.csv')
    callloop()
if day == "Friday":
    df = pd.read_csv('Friday.csv')
    callloop()


#themacn git-hub
    # author : franklin ettani christopher  
          
         




    
    
    
