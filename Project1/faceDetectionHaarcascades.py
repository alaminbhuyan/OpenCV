import cv2
import time

# Load the Cascade Classifier
face_cascade = cv2.CascadeClassifier("Haarcascades/haarcascade_frontalface_default.xml")

# Capture video
# capture_video = cv2.VideoCapture("Video/video4.mp4")

# Capture video from webcam
capture_video = cv2.VideoCapture(0)

pTime = 0

while True:
    success, frame = capture_video.read()
    # print(frame)
    cTime = time.time()
    # print("The cTime is: ", cTime)
    fps = 1 / (cTime - pTime)
    # print("The fps: ", fps)
    pTime = cTime
    # Convert color frame into gray
    gray_img = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(image=gray_img, scaleFactor=1.1, minNeighbors=6)
    # print('The faces: ',faces)

    cv2.putText(img=frame, text=f"FPS: {int(fps)}", org=(28, 55), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                color=(0, 255, 0), thickness=2)

    # Display Rectangle
    for (x, y, width, height) in faces:
        cv2.rectangle(img=frame, pt1=(x, y), pt2=(x + width, y + height), color=(255, 0, 255), thickness=3)

    # Display Image
    cv2.imshow(winname="Face Detect Image", mat=frame)  # mat= image matrix
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object
capture_video.release()
cv2.destroyAllWindows()
