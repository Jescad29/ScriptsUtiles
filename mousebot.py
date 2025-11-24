import pyautogui as botMouse
import time 
import random
import webbrowser


webbrowser.open('https://www.youtube.com/watch?v=GOEnEg8WzwY&list=RDGOEnEg8WzwY&start_radio=1')

while True:
    print(botMouse.position())
    x = 504
    y = 579
    
    botMouse.moveTo(x, y, duration=0.5)
    time.sleep(2)
    
    botMouse.click()