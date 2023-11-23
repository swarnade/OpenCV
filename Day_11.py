#importing Opencv
import cv2 as cv
#import NumPy
import numpy as np
# Read The Image 
img=cv.imread('img.jpeg')
#Convert The Image From RGB To Grey
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#Show The Grey Image
cv.imshow("Gray",gray)
#Runs The Loop For Infinity Times
cv.waitKey(0)