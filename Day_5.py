# Import OpenCV 
import cv2 as cv
# Initialize WebCam 
video =cv.VideoCapture(0)
#Funtion For Scale
def videorescale(w,h,capture):
#Scale Width Value
  capture.set(3,w)
#Scale Height Value 
  capture.set(4,h)
# Call The Rescale Funtion
videorescale(1920,1080,video)
# Runs Till True
while True:
# Read the WebCam Frame by Frame
  isTrue,frame=video.read()
# Display the WebCam 
  cv.imshow("Vid",frame)
# Break if “d” is pressed 
  if(cv.waitKey(20) & 0xff==ord('d')):
# Exits the code
    break
# Stoping Capturing
video.release
# ClosePython Windows
cv.destroyAllWindows
#Infinity Loop
cv.waitKey(0)






