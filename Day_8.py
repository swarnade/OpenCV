#importing Opencv
import cv2 as cv
#import NumPy
import numpy as np
#Creating A Blank image
blank_image=np.zeros((1080,1920,3),dtype='uint8')
# Draw a Rectangle
cv.rectangle(blank_image,(400,400),(600,600),(0,0,255), thickness=3)
#Show The Code
cv.imshow('Blank Image',blank_image)
#Runs For Infinity
cv.waitKey(0)
