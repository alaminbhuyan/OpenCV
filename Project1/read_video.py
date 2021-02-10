import cv2
import numpy

framWidth = 640
framHeight = 480
cap = cv2.VideoCapture("image_examples/cars.avi")
while cap.isOpened():
    success,frame = cap.read()
    frame_size = cv2.resize(src=frame,dsize=(framWidth,framHeight))
    cv2.imshow(winname="Test Video",mat=frame_size)
    if cv2.waitKey(1)==13:
        break
cv2.destroyAllWindows()