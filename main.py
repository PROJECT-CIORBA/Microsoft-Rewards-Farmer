import pyautogui
import subprocess
import random
import time


a = 0



subprocess.call(['C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'])
while a <= 10:
    raw_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    list = random.choice(raw_list)
    time.sleep(1)
    pyautogui.write(list)
    pyautogui.press('enter')
    time.sleep(1.5)
    pyautogui.hotkey('ctrl', 't')
    pyautogui.hotkey('ctrl', '1')
    pyautogui.hotkey('ctrl', 'w')
    a += 1
b = 0
while b <= 30:
    pyautogui.hotkey("ctrl", "t")
    pyautogui.write("https://www.bing.com/news/?form=ml11z9&crea=ml11z9&wt.mc_id=ml11z9&rnoreward=1&rnoreward=1")
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', '1')
    time.sleep(0.25)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(1)
    raw_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    list = random.choice(raw_list)
    pyautogui.write(list)
    pyautogui.press('enter')
    time.sleep(1.5)
    pyautogui.hotkey('ctrl', 't')
    pyautogui.hotkey('ctrl', '1')
    pyautogui.hotkey('ctrl', 'w')
    b += 3
pyautogui.hotkey('alt', 'f4')