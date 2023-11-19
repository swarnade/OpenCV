# Import OpenCV 
import cv2 as cv

# Initialize Image 
img=cv.imread(‘image1.jpg’)

# Dispaly The Image
cv.imshow(‘Image 1’,img)

#Dsiplay For Infinity Time
cv.waitKey(0)

