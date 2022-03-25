import cv2

# Load trained cascade classifier
eye_detect = cv2.CascadeClassifier("Haarcascades/haarcascade_eye.xml")

# Cpature from video
# cap_video = cv2.VideoCapture("Video/video4.mp4")

# Capture from webcam
cap_video = cv2.VideoCapture(0)

while True:
    # read frame/image from camera
    success, frames = cap_video.read()
    # no frame then brak loop
    if success == 0:
        break
    # Convert color image into grayscale
    gray_img = cv2.cvtColor(src=frames, code=cv2.COLOR_BGR2GRAY)
    # Detect faces ROI
    eyes = eye_detect.detectMultiScale(image=frames, scaleFactor=1.2, minNeighbors=5)
    # Draw rectangle around the eyes
    for (x, y, width, height) in eyes:
        cv2.rectangle(img=frames, pt1=(x, y), pt2=(x + width, y + height), color=(255,0,245), thickness=2)
    # Show image
    cv2.imshow(winname="Live Eye Detection", mat=frames)
    # wait to close window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap_video.release()
cv2.destroyAllWindows()