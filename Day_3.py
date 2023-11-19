# Import OpenCV 
import cv2 as cv

# Initialize WebCam 
video =cv.VideoCapture(0)

# Runs Till True
while True:
# Read the WebCam Frame by Frame
  isTrue,frame=video.read()
# Display the WebCam 
  cv.imshow("Web Cam",frame)

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




