#opencv
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

img = cv2.imread("exori gran-3.png")
img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_red = np.array(5,9,23)
upper__red = np.array(255,9,23)

mask = cv2.inRange(hsv, lower_red, upper_red)

result = cv2.bitwise_and(frame, frame, mask = mask)



cv2.imshow('frame', frame)
cv2.imshow('mask', mask)
cv2.imshow('result', result)
cv2.waitKey(0)





#resultado = pytesseract.image_to_boxes(img)

#print(resultado)

