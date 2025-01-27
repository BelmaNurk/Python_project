import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread(r"C:\Users\Korisnik\OneDrive\Desktop\Belma_Nurkic_zadaca2\zadatak2.jpg")

img2 = cv2.imread(r"C:\Users\Korisnik\OneDrive\Desktop\Belma_Nurkic_zadaca2\zadatak2.jpg", cv2.IMREAD_GRAYSCALE)

(thresh, blackAndWhiteImage) = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY)
(thres, thresh_inv) = cv2.threshold(img2, 100, 255, cv2.THRESH_BINARY_INV)
adaptive_tresh = cv2.adaptiveThreshold(img2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 3)
    

cv2.imshow('Original', img)
cv2.imshow('Gray image', img2)
cv2.imshow('Black and white image', blackAndWhiteImage)
cv2.imshow('Thresholded inverse', thresh_inv)
cv2.imshow('Adaptive thresholding', adaptive_tresh)

cv2.waitKey(0)
