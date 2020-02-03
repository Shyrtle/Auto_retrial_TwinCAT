import pyautogui
from time import sleep
import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = Image.open("C:\\Users\\jhemsley\\Pictures\\cap.jpg")
greyImg = img.convert('L')
greyImg.save('greyImg.jpg')
new_size = tuple(2*x for x in img.size)
greyImg = img.convert('L')
greyImg.save('greyImg.jpg')
img2 = Image.open('greyImg.jpg')
img2 = img2.resize(new_size, Image.ANTIALIAS)
text2 = pytesseract.image_to_string(img2)
print(text2)
