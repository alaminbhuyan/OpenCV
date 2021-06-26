import cv2
import numpy as np
import requests
import time
import mediapipe as mp

class MyfaceDetector:
    def __init__(self, min_detect_confidence=0.5):
        self.min_detect_confidence = min_detect_confidence
        self.faceDetection = mp.solutions.face_detection.FaceDetection(self.min_detect_confidence)
        self.mpDraw = mp.solutions.drawing_utils

    def findFaces(self, img, draw=True):
        imgRGB = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2RGB)
        results = self.faceDetection.process(image=imgRGB)
        # Now we capture bounding box for all faces at a time
        bboxs = []
        if results.detections:
            for id, detection in enumerate(results.detections):
                bboxCome = detection.location_data.relative_bounding_box
                imgHeight, imgWidth, imgChennel = img.shape
                bbox = int(bboxCome.xmin * imgWidth), int(bboxCome.ymin * imgHeight), \
                       int(bboxCome.width * imgWidth), int(bboxCome.height * imgHeight)
                bboxs.append([id, bbox, detection.score])
                if draw:
                    img = self.fancyDraw(img, bbox)
                cv2.putText(img=img, text=f"{int(detection.score[0] * 100)}%", org=(bbox[0], bbox[1] - 20),
                            fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(0, 255, 0), thickness=2)
        return (img, bboxs)

    def fancyDraw(self, img, bbox, l=30, thickness=5, rectangle_thikness=1):
        x, y, width, height = bbox
        x1, y1 = x + width, y + height

        cv2.rectangle(img, bbox, (255, 0, 255), rectangle_thikness)
        # Top Left  x,y
        cv2.line(img=img, pt1=(x, y), pt2=(x + l, y), color=(255, 0, 255), thickness=thickness)
        cv2.line(img=img, pt1=(x, y), pt2=(x, y + l), color=(255, 0, 255), thickness=thickness)
        # Top Right  x1,y
        cv2.line(img=img, pt1=(x1, y), pt2=(x1 - l, y), color=(255, 0, 255), thickness=thickness)
        cv2.line(img=img, pt1=(x1, y), pt2=(x1, y + l), color=(255, 0, 255), thickness=thickness)
        # Bottom Left  x,y1
        cv2.line(img=img, pt1=(x, y1), pt2=(x + l, y1), color=(255, 0, 255), thickness=thickness)
        cv2.line(img=img, pt1=(x, y1), pt2=(x, y1 - l), color=(255, 0, 255), thickness=thickness)
        # Bottom Right  x1,y1
        cv2.line(img=img, pt1=(x1, y1),pt2= (x1 - l, y1), color=(255, 0, 255), thickness=thickness)
        cv2.line(img=img, pt1=(x1, y1),pt2= (x1, y1 - l), color=(255, 0, 255), thickness=thickness)
        return img

def main():
    url = "http://192.168.0.101:8080/shot.jpg"
    width, height = 650, 650
    pTime = 0
    # Create the class object
    detector = MyfaceDetector(min_detect_confidence=0.7)
    while True:
        # success, img = capture_video.read()
        r = requests.get(url=url)
        img_arr = np.array(bytearray(r.content), dtype=np.uint8)
        img = cv2.imdecode(buf=img_arr, flags=-1)
        img, bboxs = detector.findFaces(img=img)
        print(bboxs)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img=img, text=f"FPS: {int(fps)}", org=(35, 70), fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=2,color=(0, 255, 0),thickness=2)
        img_resize = cv2.resize(src=img, dsize=(width, height))
        cv2.imshow("My img", img_resize)
        cv2.waitKey(1)


if __name__ == '__main__':
    main()