import cv2
import numpy as np

# create an image with white backgroung
img = np.ones((240,240,3)) # array of size 240, 240 with same values
cv2.line(img,(0,0),(230,230),(0,0,255),2) # draw red line accross the image
cv2.circle(img,(120,120),50,(200,0,0),2) # draw blue circle of radius 50 at center
cv2.rectangle(img,(70,150),(110,200),(0,255,0),-1) # draw green rectangle box 
# write text on the image
cv2.putText(img,'NAF HACKERS',(15,120),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,250),2)
img2 = img[50:170,70:170] # cut only Region of Interest from the image
cv2.imshow('result', img2)   # show the image
cv2.waitKey()               # wait for ke press
