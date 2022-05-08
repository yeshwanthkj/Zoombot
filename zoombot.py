import subprocess
import pyautogui
import pandas as pd
import time
from datetime import datetime

def sign_in(meeting_id,pswrd):
    #opening zoom
    subprocess.call(r"C:\Users\ABINAV YESWANTH\AppData\Roaming\Zoom\bin\Zoom")
    time.sleep(4)
    #click join
    join_btn = pyautogui.locateCenterOnScreen('join.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    #entering meeting id
    m_id_btn = pyautogui.locateCenterOnScreen('m_id.png')
    pyautogui.moveTo(m_id_btn)
    pyautogui.click()
    pyautogui.write(meeting_id)
    #media
    media_btn = pyautogui.locateAllOnScreen('tick.png')
    for btn in media_btn:
        pyautogui.moveTo(btn)
        pyautogui.click()
        time.sleep(1)
    #click join
    join_btn = pyautogui.locateCenterOnScreen('join2.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    time.sleep(8)
    #entering password
    pswd_btn = pyautogui.locateCenterOnScreen('pswd.png')
    pyautogui.moveTo(pswd_btn)
    pyautogui.click()
    pyautogui.write(pswrd)
    pyautogui.press('enter')
#reading from csv file
df=pd.read_csv('schedule.csv')
while True:
    now=datetime.now().strftime("%H:%M")
    if now in str(df['timing']):
        row=df.loc[df['timing']==now]
        m_id=str(row.iloc[0,1])
        pwd=str(row.iloc[0,2])
        sign_in(m_id,pwd)
        time.sleep(40)
        print("signed in")
                                    
    
    
        
    


