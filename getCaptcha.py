import pytesseract
import sys
import argparse
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
try:
    import Image
except ImportError:
    from PIL import Image
from subprocess import check_output

path = "C:\\Users\\jhemsley\\Pictures\\cap.jpg"
# def resolve(path):
# 	print("Resampling the Image")
# 	check_output(['magick', path, '-resample', '600', path])
# 	return pytesseract.image_to_string(Image.open(path))
#
# print(resolve(path))
img = cv2.imread("C:\\Users\\jhemsley\\Pictures\\cap.jpg")
text = pytesseract.image_to_string(img)
print(text)
