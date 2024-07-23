import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread(r"C:\Users\Korisnik\OneDrive\Desktop\Belma_Nurkic_zadaca2\zadatak2.jpg")
cv2.imshow('Original', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
combined_sobel = cv2.bitwise_or(sobelx, sobely)
cv2.imshow('Sobelx', sobelx)
cv2.imshow('Sobely', sobely)
cv2.imshow('Combined Sobel', combined_sobel)
cv2.waitKey(0)

#Canny
canny = cv2.Canny(gray, 150, 175)
cv2.imshow('Canny', canny)
cv2.waitKey(0)

# Labplacian filter
lap = cv2.Laplacian(gray, cv2.CV_64F)
cv2.imshow('Laplacian', lap)
cv2.waitKey(0)

