import cvzone
import cv2

fpsReader = cvzone.FPS()


cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    fps, frame = fpsReader.update(img=frame, pos=(50, 80), color=(0, 255, 0), scale=2, thickness=2)
    cv2.imshow(winname="Image", mat=frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()