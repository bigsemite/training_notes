import cv2

# load image
pic =cv2.imread('navy_logo.png')
# line on image: draw white line on the picture
pic = cv2.line(pic, (10,10),(200,300), (255,255,255),2)
cv2.imshow('DC',pic)
cv2.waitKey()
    
