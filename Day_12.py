#importing Opencv
import cv2 as cv
#import NumPy
import numpy as np
# Read The Image 
img=cv.imread('img.jpeg')
#Convert The Image From Normal To Blur
blur=cv.GaussianBlur(img,(3,9),cv.BORDER_DEFAULT)
#Show The Blur Image
cv.imshow("Blur",blur)
#Runs The Loop For Infinity Times
cv.waitKey(0)