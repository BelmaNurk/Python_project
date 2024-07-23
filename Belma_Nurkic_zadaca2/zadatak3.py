import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread(r"C:\Users\Korisnik\OneDrive\Desktop\Belma_Nurkic_zadaca2\zadatak2.jpg")
cv2.imshow('Original', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', gray)

histr = cv2.calcHist([gray], [0], None, [256], [0,256])
plt.figure()
plt.xlabel('Bins')
plt.ylabel('Nummber of pixels')
plt.plot(histr)
plt.show()

cv2.waitKey(0)