import cv2

face_classifier = cv2.CascadeClassifier("Haarcascades/haarcascade_frontalface_default.xml")

image = cv2.imread(filename="image_example/alamin2.jpg")

gray_img = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)

faces = face_classifier.detectMultiScale(image=gray_img, scaleFactor=1.3, minNeighbors=5)


# we iterate through our faces array and draw a rectangle
# over each face in faces
l = 25
for (x, y, width, height) in faces:
    # bbox = (x, y, width, height)
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

    # cv2.rectangle(image, bbox, color=(127, 0, 255), thickness=2)

cv2.imshow("Face Detection", image)
cv2.waitKey()

cv2.destroyAllWindows()
