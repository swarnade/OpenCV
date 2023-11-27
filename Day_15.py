#importing Opencv
import cv2 as cv
#import NumPy
import numpy as np  
# Read The Image 
img=cv.imread('img.jpeg')
#Convert The Image From Normal To Scaled Size
resize=cv.resize(img,(500,500))
#Show The Resized Image
cv.imshow("Resized",resize)
#Runs The Loop For Infinity Times
cv.waitKey(0)