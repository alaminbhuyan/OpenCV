import cv2

# Load the Cascade Classifier
face_cascade = cv2.CascadeClassifier("Haarcascades/haarcascade_frontalface_default.xml")
eye_detector = cv2.CascadeClassifier("Haarcascades/haarcascade_eye.xml")

# Capture video from webcam
capture_video = cv2.VideoCapture(0)

while True:
    success, frame = capture_video.read()

    if not success:
        break
    else:
        # Convert color frame into gray
        gray_frame = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = face_cascade.detectMultiScale(image=gray_frame, scaleFactor=1.1, minNeighbors=6)
        # Display Rectangle
        for (x, y, width, height) in faces:
            cv2.rectangle(img=frame, pt1=(x, y), pt2=(x + width, y + height), color=(255, 0, 255), thickness=2)
            eyes = eye_detector.detectMultiScale(image=frame, scaleFactor=1.2, minNeighbors=5)
            for (x, y, width, height) in eyes:
                cv2.rectangle(img=frame, pt1=(x, y), pt2=(x + width, y + height), color=(255, 0, 245), thickness=2)

        # Show image
        cv2.imshow(winname="Live Face & Eye Detection", mat=frame)
        # wait to close window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the VideoCapture object
capture_video.release()
cv2.destroyAllWindows()