import pyautogui
import subprocess
import random
import time


a = 0



subprocess.call(['C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'])
while a <= 10:
    raw_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    list = random.choice(raw_list)
    time.sleep(1.5)
    pyautogui.write(list)
    pyautogui.press('enter')
    time.sleep(1.5)
    pyautogui.hotkey('ctrl', 't')
    pyautogui.hotkey('ctrl', '1')
    pyautogui.hotkey('ctrl', 'w')
    a += 1