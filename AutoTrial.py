import pyautogui
from time import sleep
import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
print("Press Ctrl-C to quit.")

print(pyautogui.size())
width, height = pyautogui.size()

sleep(5)
print(pyautogui.position())

def dragTo(from_x, from_y, to_x, to_y):
    try:
        pyautogui.mouseDown(from_x, from_y)
    except PermissionError:
        pass

    try:
        pyautogui.mouseUp(to_x, to_y)
    except PermissionError:
        pass


# pyautogui.click(-1167, 262)
# pyautogui.typewrite('Hello world!')

# startMenu
pyautogui.click(27, 1059)
# visualStudio =
pyautogui.click(399, 853)
sleep(20)
# teamExplorer =
pyautogui.click(157, 1002)
sleep(5)
# sourceControlExplorer
pyautogui.click(128, 357)
# asm6
pyautogui.click(535, 242, button='right') # Right Click
# sleep(2)
# getLatestVersion
pyautogui.click(589, 251)
sleep(5)
pyautogui.press('enter')
# topASM6
pyautogui.doubleClick(768, 249) # Double Click
# openProjASM6
pyautogui.doubleClick(779, 307) # Double Click
sleep(30)
# solutionExplorer
pyautogui.click(57, 1002)
# license
pyautogui.doubleClick(117, 248) # Double Click
# trialLicense
pyautogui.click(593, 414)
sleep(1)
# Use Snipping Tool to capture letters.
# startMenu
pyautogui.click(27, 1059)
# snipAndSketch
pyautogui.click(588, 599)
sleep(1)
# newSnip
pyautogui.click(37, 48)
sleep(1)

# rectSnip
pyautogui.click(865, 26)
# selectArea
dragTo(812, 512, 1015, 571)

# # windowSnip
# pyautogui.moveTo(959, 27)
# pyautogui.click(959, 27)
# sleep(1)
# # CAPTCHAWindow
# pyautogui.moveTo(961, 477, duration=1)
# pyautogui.click(961, 477)
# sleep(1)
# pyautogui.moveTo(961, 477)
# pyautogui.click(961, 477)
# sleep(1)
# # crop
# pyautogui.click(1090, 50)
# sleep(1)
# # rCropping = # Start (1116, 490) End (944, 552) # Click and Drag pyautogui.dragTo()
# dragTo(1116, 490, 944, 552)
# sleep(1)
# # cropDone
# pyautogui.click(1859, 54)
# sleep(1)
# save
pyautogui.click(1770, 51)
sleep(1)
# picType # Click, Press 'J', Click
pyautogui.click(938, 462)
pyautogui.typewrite('j')
pyautogui.click(938, 462)

# picName
pyautogui.click(325, 434)
# type "cap"
pyautogui.typewrite('cap')
# outName
pyautogui.click(38, 435)
# clickSave
pyautogui.click(792, 507)
#clickOverwrite
pyautogui.click(1009, 530)
# closeSnip
pyautogui.click(1895, 17)


img = Image.open("C:\\Users\\jhemsley\\Pictures\\cap.jpg")
greyImg = img.convert('L')
greyImg.save('greyImg.jpg')
new_size = tuple(2*x for x in img.size)
greyImg = img.convert('L')
greyImg.save('greyImg.jpg')
img2 = Image.open('greyImg.jpg')
img2 = img2.resize(new_size, Image.ANTIALIAS)
text = pytesseract.image_to_string(img2)


# img = cv2.imread("C:\\Users\\jhemsley\\Pictures\\cap.jpg")
# text = pytesseract.image_to_string(img)
sleep(5)
print(text)

#
# # backInTrial
pyautogui.click(849, 558)
# # Type code
pyautogui.typewrite(text)
# clickOK
#pyautogui.click(1065, 505)
