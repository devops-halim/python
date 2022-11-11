import pyautogui as py
import time , string , random

characters = string.ascii_letters
length = 10
number = input ("No of messages: ")
for i in range(20):
    output = " ".join(random.sample(characters,length))
    py.typewrite(output)
    py.press('Enter')
    time.sleep(0)