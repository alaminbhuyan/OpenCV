import cv2
import time

# Load the Cascade Classifier
face_cascade = cv2.CascadeClassifier("Haarcascades/haarcascade_frontalface_default.xml")

# Capture video
# capture_video = cv2.VideoCapture("Video/video4.mp4")

# Capture video from webcam
capture_video = cv2.VideoCapture(0)

pTime = 0


def designRectangle(image, faces):
    # Display Rectangle
    l = 25
    for (x, y, width, height) in faces:
        x1, y1 = x + width, y + height
        cv2.rectangle(img=image, pt1=(x, y), pt2=(x + width, y + height), color=(127, 0, 255), thickness=1)
        # Top Left  x,y
        cv2.line(img=image, pt1=(x, y), pt2=(x + l, y), color=(255, 0, 0), thickness=5)
        cv2.line(img=image, pt1=(x, y), pt2=(x, y + l), color=(255, 0, 0), thickness=4)
        # Top Right  x1,y
        cv2.line(img=image, pt1=(x1, y), pt2=(x1 - l, y), color=(255, 0, 0), thickness=5)
        cv2.line(img=image, pt1=(x1, y), pt2=(x1, y + l), color=(255, 0, 0), thickness=4)
        # Bottom Left  x,y1
        cv2.line(img=image, pt1=(x, y1), pt2=(x + l, y1), color=(255, 0, 0), thickness=5)
        cv2.line(img=image, pt1=(x, y1), pt2=(x, y1 - l), color=(255, 0, 0), thickness=4)
        # Bottom Right  x1,y1
        cv2.line(img=image, pt1=(x1, y1), pt2=(x1 - l, y1), color=(255, 0, 0), thickness=5)
        cv2.line(img=image, pt1=(x1, y1), pt2=(x1, y1 - l), color=(255, 0, 0), thickness=4)
    return image


while True:
    success, frame = capture_video.read()
    if success == True:
        cTime = time.time()
        # print("The cTime is: ", cTime)
        fps = 1 / (cTime - pTime)
        # print("The fps: ", fps)
        pTime = cTime
        # Convert color frame into gray
        gray_img = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = face_cascade.detectMultiScale(image=gray_img, scaleFactor=1.1, minNeighbors=5)
        # print('The faces: ',faces)

        cv2.putText(img=frame, text=f"FPS: {int(fps)}", org=(28, 55), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                    color=(0, 255, 0), thickness=2)

        image = designRectangle(image=frame, faces=faces)

        # Display Image
        cv2.imshow(winname="Face Detect Image", mat=image)  # mat= image matrix
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the VideoCapture object
capture_video.release()
cv2.destroyAllWindows()
