import cv2

cam = cv2.VideoCapture(0)
while 1:
    n,frame=cam.read()
    cv2.imshow("MY camera",frame)
    cv2.waitKey(1)


    