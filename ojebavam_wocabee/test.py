from PIL import Image, ImageGrab
import cv2 as cv
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\\tesseract.exe'

img = ImageGrab.grab(bbox=(600, 255, 1350, 560))
img_np = cv.cvtColor(np.array(img), cv.COLOR_BGR2GRAY)
print(pytesseract.image_to_string(img_np).lower().replace("\n", ""))
cv.imshow("kys", img_np)
cv.waitKey(0)
