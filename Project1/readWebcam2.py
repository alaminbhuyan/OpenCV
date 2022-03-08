import cv2

video = cv2.VideoCapture(0)

width, height = 600, 500

while True:
    success, frame = video.read()
    frame_size = cv2.resize(frame, (width, height))
    cv2.imshow('img', frame_size)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()