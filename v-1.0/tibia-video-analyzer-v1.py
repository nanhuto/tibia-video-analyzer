#opencv
import cv2
import pytesseract
import numpy as np
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

img = cv2.imread('exori gran-4.png')
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower = np.array([55,50,200])
upper = np.array([70,250,255])

mask = cv2.inRange(imgHSV, lower, upper)

mask2 = pytesseract.image_to_string(mask)
print(mask2)


cv2.imshow("res", mask)
cv2.waitKey(0)












