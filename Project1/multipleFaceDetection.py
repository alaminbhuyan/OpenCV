import cv2

face_classifier = cv2.CascadeClassifier("Haarcascades/haarcascade_frontalface_default.xml")

# color_img = cv2.imread(filename="image_example/Trump.jpg")
color_img = cv2.imread(filename="image_example/multipleFace3.jpg")

gray_img = cv2.cvtColor(src=color_img, code=cv2.COLOR_BGR2GRAY)


faces = face_classifier.detectMultiScale(image=gray_img, scaleFactor=1.3, minNeighbors=5)

# we iterate through our faces array and draw a rectangle
# over each face in faces
for (x, y, width, height) in faces:
    cv2.rectangle(img=color_img, pt1=(x, y), pt2=(x + width, y + height), color=(127, 0, 255), thickness=2)

cv2.imshow("Face Detection", color_img)
cv2.waitKey()

cv2.destroyAllWindows()
