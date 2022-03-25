import cv2

# Load trained cascade classifier
eye_detect = cv2.CascadeClassifier("Haarcascades/haarcascade_eye.xml")

# Read the Image
color_img = cv2.imread(filename="image_example/alamin2.jpg")

# Convert color image into gray
gray_img = cv2.cvtColor(src=color_img, code=cv2.COLOR_BGR2GRAY)

# extract the eyes
eyes = eye_detect.detectMultiScale(image=gray_img, scaleFactor=1.3, minNeighbors=7)
# Draw rectangle around the eyes
for (x, y, width, height) in eyes:
    cv2.rectangle(img=color_img, pt1=(x, y), pt2=(x + width, y + height), color=(0,255,0), thickness=2)

# Show image
cv2.imshow(winname="Eye detect Image", mat=color_img)

# wait to close window
cv2.waitKey()
# Destroy the all open window
cv2.destroyAllWindows()