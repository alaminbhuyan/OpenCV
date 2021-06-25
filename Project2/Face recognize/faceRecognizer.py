import cv2
import numpy as np
import time
import mediapipe as mp

def showVideo(path):
    frame_height = 700
    frame_width = 700
    capture = cv2.VideoCapture(path)
    past_Time = 0

    mpFaceDetection = mp.solutions.face_detection
    mpDraw = mp.solutions.drawing_utils
    faceDetection = mpFaceDetection.FaceDetection(min_detection_confidence=0.5)

    while capture.isOpened():
        success, frame = capture.read()

        imgRGB = cv2.cvtColor(src=frame,code=cv2.COLOR_BGR2RGB)
        results = faceDetection.process(image=imgRGB)
        print(results)

        if results.detections:
            for id, detection in enumerate(results.detections):
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = frame.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih),int(bboxC.width * iw), int(bboxC.height * ih)
                cv2.rectangle(frame,bbox,(255,0,255),2)
                cv2.putText(frame,f"{int(detection.score[0]*100)}%",
                            (bbox[0],bbox[1]-20), cv2.FONT_HERSHEY_PLAIN,
                            2,(255,0,255),2)
        current_time = time.time()
        fps = 1 / (current_time - past_Time)
        past_Time = current_time
        cv2.putText(img=frame, text=f"FPS: {int(fps)}", org=(20, 70),fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=3, color=(0, 255, 0), thickness=2)
        frame_resize = cv2.resize(src=frame, dsize=(frame_width, frame_height))
        cv2.imshow(winname="Tiger running video", mat=frame_resize)
        cv2.waitKey(1)
    cv2.destroyAllWindows()

path = "Videos/video5.mp4"
showVideo(path=path)
