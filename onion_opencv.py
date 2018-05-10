# user:hu

import cv2 as cv
import numpy as np


def nothing(x):
    pass


def save_video():
    cap = cv.VideoCapture(1)
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('onion_video2.avi', fourcc, 20.0, (640, 480))
    while True:

        ret, frame = cap.read()
        if ret:
            frame = cv.flip(frame, 0)
            out.write(frame)
            cv.imshow('video', frame)
            if cv.waitKey(1) & 0xff == ord('q'):
                break
        else:
            break
    cap.release()
    out.release()
    cv.destroyAllWindows()


def save_video2():
    cap = cv.VideoCapture(0)
    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            frame = cv.flip(frame, 0)
            # write the flipped frame
            out.write(frame)
            cv.imshow('frame', frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    # Release everything if job is finished
    cap.release()
    out.release()
    cv.destroyAllWindows()


def by_camera():
    cap = cv.VideoCapture(1)
    cv.namedWindow('image')
    cv.createTrackbar('N_thresh', 'image', 20, 200, nothing)
    cv.createTrackbar('ON/OFF', 'image', 0, 1, nothing)
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('onion_video.avi', fourcc, 20.0, (640, 480))

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
    out.release()
    cv.destroyAllWindows()


def by_video_file():
    file_path = 'output.avi'
    # file_path = '/Users/huyangjie/Downloads/opencv-3.4.0/samples/data/vtest.avi'
    cap = cv.VideoCapture(file_path)
    print(cap)
    while True:
        ret, frame = cap.read()
        cv.imshow('video_file', frame)
        if cv.waitKey(1) & 0xff == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    by_video_file()
