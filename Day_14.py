#importing Opencv
import cv2 as cv
#import NumPy
import numpy as np
# Read The Image 
img=cv.imread('img.jpeg')
#Convert The Image From Normal To Dilate
dilate=cv.dilate(img,(3,3),iterations=3)
#Show The Edged Image
cv.imshow("Dilatted",dilate)
#Runs The Loop For Infinity Times
cv.waitKey(0)