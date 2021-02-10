import cv2

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)

while True:
    success,frame = cap.read()
    cv2.imshow("Result",frame)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

cv2.destroyAllWindows()