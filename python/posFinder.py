import pyautogui
from time import sleep
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
print("Press Ctrl-C to quit.")

print(pyautogui.size())
width, height = pyautogui.size()


for x in range(0,5):
    sleep(5)
    print(pyautogui.position())
