# https://github.com/cvzone/cvzone

import cv2
from cvzone.FaceDetectionModule import FaceDetector

capture_video = cv2.VideoCapture(0)
detector = FaceDetector()

while True:
    success, frame = capture_video.read()
    img, bboxs = detector.findFaces(img=frame)
    if bboxs:
        # bboxInfo - "id","bbox","score","center"
        center = bboxs[0]["center"]
        cv2.circle(img=frame, center=center, radius=5, color=(255, 255, 0), thickness=None, lineType=cv2.FILLED)

    cv2.imshow(winname="Image", mat=frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


capture_video.release()
cv2.destroyAllWindows()