import numpy as np
import matplotlib.pyplot as plt
import cv2

img=cv2.imread(r"C:\Users\Korisnik\OneDrive\Desktop\Belma_Nurkic_zadaca2\raketa1.jpg")
cv2.imshow('Original', img)

#Gauss
gaussian = cv2.GaussianBlur (img, (9,9), 0)
cv2.imshow ('Gaussian blur', gaussian)
#cv2.waitKey(0)

#Median
median = cv2.medianBlur (img, 3)
cv2.imshow ('Median', median)
#cv2.waitKey(0)

#Averaging
average = cv2.blur(img, (4,4))
cv2.imshow ('Average', average)
cv2.waitKey(0)
