import cv2

pic = cv2.imread("navy_logo.png")   # Read image from a file
pic.tofile('f2.txt', sep=',')     # save digital values of image as a matrix
print(pic.shape)                    # get the size of the given image
cv2.imshow('win',pic)               # display the image frame in a window named "win"
cv2.waitKey()                   # suspend output operation until any key is pressed
t1= pic[0:100,:,:] +200         # cut the picture and make the cut picture more bright
cv2.imshow('win',t1)                
cv2.waitKey()