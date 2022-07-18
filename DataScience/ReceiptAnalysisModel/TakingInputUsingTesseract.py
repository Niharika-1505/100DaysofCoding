import pytesseract
import cv2 as cv
import numpy as np

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR/tesseract.exe'
image = cv.imread("./InputData/Asda_Receipt_1.jpeg")
d = pytesseract.image_to_string(image)
print(d)
