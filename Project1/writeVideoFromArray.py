import numpy as np
import cv2


width, height = 720, 1280
channel, fps, sec = 3, 30, 5

fourcc = cv2.VideoWriter_fourcc(*'MP42')

video = cv2.VideoWriter('Video\\test.mp4', fourcc, float(fps), (width, height))

for frame_count in range(fps*sec):
    img = np.random.randint(low=0, high=255, size=(height, width, channel), dtype=np.uint8)
    video.write(image=img)

video.release()