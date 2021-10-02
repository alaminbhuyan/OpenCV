import cv2
import numpy as np

fram_width = 650
fram_height = 480

# capture the video
capture = cv2.VideoCapture("image_example/all video/cars.avi")

# create the loop
while capture.isOpened():
    # 'success' return 'true' value until the video is end if video is end then return 'false'
    success, frame = capture.read()
    frame_size = cv2.resize(src=frame, dsize=(fram_width,fram_height))
    cv2.imshow(winname="Test video", mat=frame_size)
    if cv2.waitKey(1)==13:
        break
cv2.destroyAllWindows()
