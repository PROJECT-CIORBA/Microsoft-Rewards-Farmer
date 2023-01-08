import pyautogui
import subprocess
import random
import time


a = 0


#Opens Microsoft Edge, for obvious reasons.
subprocess.call(['C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'])
#Searchs random letters 10 times.
while a <= 10:
    #Probably could've been written more efficiently.
    raw_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', "1", "2", "3","4","5","6","7","8","9","0"]
    list = random.choice(raw_list)
    time.sleep(1)
    pyautogui.write(list)
    pyautogui.press('enter')
    time.sleep(1.5)
    #Browser shortcuts, my favourite.
    pyautogui.hotkey('ctrl', 't')
    pyautogui.hotkey('ctrl', '1')
    pyautogui.hotkey('ctrl', 'w')
    a += 1
b = 0
#Uses Bing (;-;), and does the same thing.
while b <= 10:
    #Opens the url.
    #Again, could've been written more efficiently.
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
    #Same stuff as last time.
    raw_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', "1", "2", "3","4","5","6","7","8","9","0"]
    list = random.choice(raw_list)
    pyautogui.write(list)
    pyautogui.press('enter')
    time.sleep(1.5)
    pyautogui.hotkey('ctrl', 't')
    pyautogui.hotkey('ctrl', '1')
    pyautogui.hotkey('ctrl', 'w')
    b += 1
#Closes the last tab, making the browser close.
pyautogui.hotkey('ctrl', 'w')