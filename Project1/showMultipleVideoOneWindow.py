import cv2
import numpy as np

# Capture the video
capture_video = cv2.VideoCapture("Video/video4.mp4")

while True:
    success, frame = capture_video.read()
    if success:
        frame = cv2.resize(src=frame, dsize=(400,300))
        frame_2 = np.hstack((frame, frame))
        frame_3 = np.vstack((frame_2, frame_2))
        cv2.imshow(winname="Video Player", mat=frame_3)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture_video.release()
cv2.destroyAllWindows()