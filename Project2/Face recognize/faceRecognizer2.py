import cv2
import mediapipe as mp
import time

capture = cv2.VideoCapture("Videos/video3.mp4")
width , height = 700, 700
pTime = 0

# mp_face_detection = mp.solutions.face_detection
# face_detection = mp_face_detection.FaceDetection()
face_detection = mp.solutions.face_detection.FaceDetection()
mp_draw = mp.solutions.drawing_utils


while capture.isOpened():
    success, img = capture.read()
    imgRGB = cv2.cvtColor(src=img,code=cv2.COLOR_BGR2RGB)
    results = face_detection.process(image=imgRGB)
    # print(results) # this line return <class 'mediapipe.python.solution_base.SolutionOutputs'>
    # Extract the informations
    if results.detections:
        for id, detection in enumerate(results.detections):
            # BuiltIn drawing method for bounding box draw
            # mp_draw.draw_detection(image=img,detection=detection)
            # print(id, detection)
            # print(detection.score)
            # print(detection.location_data.relative_bounding_box)
            # We will create our own bounding box
            bboxCome = detection.location_data.relative_bounding_box
            imgHeight, imgWidth, imgChennel = img.shape
            # Our simple bounding box
            # we have to use pixel value not normalize value so we do that operations to achieve the pixel value
            bbox = int(bboxCome.xmin * imgWidth), int(bboxCome.ymin * imgHeight), \
                   int(bboxCome.width * imgWidth), int(bboxCome.height * imgHeight)
            # Now create the rectangle for show our bounding box
            cv2.rectangle(img,bbox,(0,255,255),2)
            # print(bbox) # this line return (338, 60, 133, 133) like this value but all time not same value return

            # Now put the text for seeing the our accuracy score
            # score mean how clearly detect our model that it's a face
            cv2.putText(img=img, text=f"{int(detection.score[0]*100)}%", org=(bbox[0],bbox[1]-20),
                        fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2,color=(0, 255, 0),thickness=2)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    # print("fps: ",fps)
    # print("ptime: ",pTime)
    cv2.putText(img=img, text=f"FPS: {int(fps)}", org=(35,70), fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=2,color=(0,255,0),
                thickness=2)
    img_resize = cv2.resize(src=img, dsize=(width, height))
    cv2.imshow("My img", img_resize)
    cv2.waitKey(1)
cv2.destroyAllWindows()

