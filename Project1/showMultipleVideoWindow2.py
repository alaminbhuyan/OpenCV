import cv2
import numpy as np


image = cv2.imread(filename="image_example/lena.png")
capture_video1 = cv2.VideoCapture("Video/video2.mp4")
capture_video2 = cv2.VideoCapture("Video/video4.mp4")
capture_video3 = cv2.VideoCapture(0)

while capture_video1.isOpened():
    res1, frame1 = capture_video1.read()
    res2, frame2 = capture_video2.read()
    res3, camera_frame = capture_video3.read()
    if res1:
        frame1 = cv2.resize(src=frame1, dsize=(400,300))
        frame2 = cv2.resize(src=frame2, dsize=(400,300))
        camera_frame = cv2.resize(src=camera_frame, dsize=(400, 300))
        image = cv2.resize(src=image, dsize=(400,300))

        frame4 = np.hstack((frame1, frame2))
        frame5 = np.hstack((camera_frame, image))
        frame6 = np.vstack((frame4, frame5))

        cv2.imshow(winname="Video Player", mat=frame6)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture_video1.release()
cv2.destroyAllWindows()