#! python3
'''randomClicker.py - a simple script that will help you fool click-spying
software at work'''

import random
import time 
import pyautogui

def click_mouse():

    print("How often should I click? Provide amount of seconds: ")
    delay1 = int(input())
    print("How often should I change the active window? Provide amount of seconds: ")
    delay2 = int(input())

    try:
        while True:
            time.sleep(random.randint(1,delay1))
            pyautogui.click()
            time.sleep(random.randint(1,delay2))
            pyautogui.hotkey('alt','tab')
            
    except KeyboardInterrupt:
    #handle the Ctrl-C exception to keep its error message from displaying
        print('\nGet back to work!')

click_mouse()
