import numpy as np
import cv2
import os


width, height = 720, 1280
channel, fps, sec = 3, 30, 5

fourcc = cv2.VideoWriter_fourcc(*'MP42')

video = cv2.VideoWriter('Video\\test.mp4', fourcc, float(fps), (width, height))

directory = ""

img_name_list = os.listdir(directory)

for _ in range(fps*sec):
    img_name = np.random.choice(img_name_list)
    img_path = os.path.join(directory, img_name)
    img = cv2.imread(filename=img_path)
    img_resize = cv2.resize(src=img, dsize=(width, height))
    video.write(image=img)

video.release()