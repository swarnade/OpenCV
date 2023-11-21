#importing Opencv
import cv2 as cv
#import NumPy
import numpy as np
#Creating A Blank image
blank_image=np.zeros((1000,1000,3),dtype='uint8')
# Draw a Circle
cv.circle(blank_image,(500,500),40,(0,0,255), thickness=3)
#Show The Code
cv.imshow('Blank Image',blank_image)
#Runs For Infinity
cv.waitKey(0)
