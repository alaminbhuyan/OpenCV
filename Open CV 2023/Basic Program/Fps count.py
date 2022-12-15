import cv2
import time

cap = cv2.VideoCapture(0)

pTime = 0 # previous time

while True:
    ret, frame = cap.read()
    cTime = time.time() # current time
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img=frame, text=f"FPS: {int(fps)}", org=(35, 70), fontFace=cv2.FONT_HERSHEY_PLAIN,
                fontScale=2, color=(255, 0, 255), thickness=2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


