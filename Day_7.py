import cv2 as cv
import numpy as np
blank_image=np.zeros((1080,1920,3),dtype='uint8')
blank_image[100:200,100:200]=255,0,0
cv.imshow('Blank Image',blank_image)
cv.waitKey(0)
