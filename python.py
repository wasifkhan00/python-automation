import pyautogui
import time
time.sleep(5)
count = 0
while count <= 60:
    pyautogui.typewrite('Reply Quick Kao')
    pyautogui.press('enter')
    count = count+1
