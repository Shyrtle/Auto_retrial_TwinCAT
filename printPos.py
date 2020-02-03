import pyautogui
from time import sleep

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
print("Press Ctrl-C to quit.")

print(pyautogui.size())
width, height = pyautogui.size()

sleep(5)
print(pyautogui.position())
