import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread(r"C:\Users\Korisnik\OneDrive\Desktop\Belma_Nurkic_zadaca2\zadatak2.jpg")
cv.imshow('Original', img)

(ret, thresh) = cv.threshold(img, 100, 255, cv.THRESH_BINARY_INV)
kernel = np.ones((5,5), np.uint8)

img_erosion = cv.erode(thresh, kernel, iterations=1)
cv.imshow ('Erosion', img_erosion)
img_dilation = cv.dilate(thresh, kernel, iterations=1)
cv.imshow ('Dilatation', img_dilation)
img_opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel)
cv.imshow ('Opening', img_opening)
img_closing = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel)
cv.imshow ('Closing', img_closing)

cv.waitKey(0)
