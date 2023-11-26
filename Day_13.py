#importing Opencv
import cv2 as cv
#import NumPy
import numpy as np
# Read The Image 
img=cv.imread('img.jpeg')
#Convert The Image From Normal To Edged
edge=cv.Canny(img,125,150)
#Show The Edged Image
cv.imshow("Edge",edge)
#Runs The Loop For Infinity Times
cv.waitKey(0)