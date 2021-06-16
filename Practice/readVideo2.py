import cv2
import numpy as np



def showVideo(path):
    frame_height = 500
    frame_width = 700

    ## load the video
    # capture = cv2.VideoCapture("image_example/all video/tiger.mp4")
    capture = cv2.VideoCapture(path)

    while capture.isOpened():
        success, frame = capture.read()
        frame_resize = cv2.resize(src=frame, dsize=(frame_width,frame_height))
        cv2.imshow(winname="Tiger running video", mat=frame_resize)
        if cv2.waitKey(1)==13:
            break
    cv2.destroyAllWindows()

path = "image_example/all video/tiger.mp4"
showVideo(path=path)