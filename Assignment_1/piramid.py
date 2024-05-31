
import pyautogui
from time import sleep

N = int(input())
sleep(2)
for i in range(1,N+1):
    for j in range(0,i):
        pyautogui.write('#', interval=0.25) 
    pyautogui.press('Enter')
   











    




