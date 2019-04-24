import pyautogui
import time
import re
import sys

imgXY = pyautogui.locateCenterOnScreen('reg_and_log.png')
pyautogui.moveTo(imgXY[0]-150, imgXY[1], duration=2)
pyautogui.click()
time.sleep(1)
'''
imgXY = pyautogui.locateCenterOnScreen('reg.png')
pyautogui.moveTo(imgXY[0], imgXY[1]+75, duration=2)
pyautogui.click()
time.sleep(1)

imgXY = pyautogui.locateCenterOnScreen('next_reg.png')
pyautogui.moveTo(imgXY[0], imgXY[1]-60, duration=2)
pyautogui.click()
pyautogui.typewrite(['9', '0', '9', '4', '8', '4', '3', '1', '2', '1',  'enter'], interval=1)
time.sleep(1)

imgXY = pyautogui.locateCenterOnScreen('kod.png')
pyautogui.moveTo(imgXY[0], imgXY[1], duration=2)
pyautogui.click()
pyautogui.typewrite(['9', '0', '9', '4', '8', '4', 'enter'], interval=1)
time.sleep(1)
'''

imgXY = pyautogui.locateCenterOnScreen('reg.png')
pyautogui.moveTo(imgXY[0], imgXY[1]-260, duration=2)
pyautogui.click()
pyautogui.typewrite(['d', 'e', 'i', 't', '9', '1', '@', 'y', 'a', 'n', 'd', 'e', 'x', '.', 'r', 'u'], interval=1)
time.sleep(1)

pyautogui.moveTo(imgXY[0], imgXY[1]-190, duration=2)
pyautogui.click()
pyautogui.typewrite(['M', '3', '2', '4', '4', 'd', 'm', 'k', 'enter'], interval=1)
time.sleep(1)

