import cv2

# read from camera
cam = cv2.VideoCapture(0)
while True:
    status, frm = cam.read()
    cv2.imshow('Win', frm)
    if cv2.waitKey(1) == 27:
        break