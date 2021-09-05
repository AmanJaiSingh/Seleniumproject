import pyautogui #pip install pyautogui
import time

data='''
paste your code here
'''

maindata = data.replace("\r", "")

time.sleep(10)
pyautogui.write(maindata)