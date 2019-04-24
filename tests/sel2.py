import pyautogui
import time
import sys
i = 0
array = []
while i<100:
    i+=1
    x = pyautogui.position().x
    y = pyautogui.position().y
    array.append([x, y])
    time.sleep(0.065)

f = open('text.txt', 'w')
for arr in array:
    f.write('x:' + str(arr[0]) + '|y:' + str(arr[1]) + '\n')
