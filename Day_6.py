#importing Opencv
import cv2 as cv
#import NumPy
import numpy as np


#Creating A Blank image
blank_image=np.zeros((1080,1920), 
dtype='uint8')



#Show The Code
cv.imshow('Blank Image',blank_image)
#Runs For Infinity
cv.waitKey(0)
