# user:hu

import cv2 as cv
import numpy as np


def nothing(x):
    pass


cap = cv.VideoCapture(0)
cv.namedWindow('image')
cv.createTrackbar('N_thresh', 'image', 20, 200, nothing)
cv.createTrackbar('ON/OFF', 'image', 0, 1, nothing)

i = 100
while True:
    num_thresh = cv.getTrackbarPos('N_thresh', 'image')
    ret, frame1 = cap.read()
    frame = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)
    _, thresh = cv.threshold(frame, num_thresh, 255, 1)
    # cv.putText(thresh, str(num_thresh), (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, 0, 2)
    _, contours, _ = cv.findContours(thresh, 1, 2)
    for cnt in contours:
        area = cv.contourArea(cnt)
        (x, y), radius = cv.minEnclosingCircle(cnt)
        if area / (3.14*(radius**2)) > 0.9 and area > 100:
            cv.circle(frame1, (int(x), int(y)), int(radius), (0, 0, 255), 2)

        # thresh = cv.cvtColor(thresh, cv.COLOR_GRAY2BGR)
    cv.imshow('image', frame1)
    if cv.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

