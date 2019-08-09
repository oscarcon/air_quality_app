# optical character recognition

import pytesseract
import cv2

img = cv2.imread('/home/huy/Desktop/captcha2.jpeg', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(pytesseract.image_to_string(img))
