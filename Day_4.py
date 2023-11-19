# Import OpenCV 
import cv2 as cv
# Initialize WebCam 
video =cv.VideoCapture(‘vid.mp4’)
#Funtion For Scale
def resize(frame,scale):
#Scale Height Value
  height=int(frame.shape[0]*scale)
#Scale Width Value 
  width=int(frame.shape[1]*scale)
#Stores Height And Width
  dim=(width,height)
#Returns Frame With a Scale
  return img _cv.resize(frame,dim, interpolation=img_cv.INTER_AREA)
                 # Runs Till True
while True:
# Read the WebCam Frame by Frame
  isTrue,frame=video.read()
# Display the WebCam 
  cv.imshow("Vid",resize(frame))
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




                         
