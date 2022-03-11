import cv2

# Create car haarcascades object
car_cascades = cv2.CascadeClassifier("Haarcascades/haarcascade_car.xml")

# Read the car Image
car_image = cv2.imread(filename="image_example/multipleCars.jpg")

# Convert the color image into gray
gray_image = cv2.cvtColor(src=car_image, code=cv2.COLOR_BGR2GRAY)

# Detect the car
cars = car_cascades.detectMultiScale(image=gray_image, scaleFactor=1.1, minNeighbors=1)

for (x, y, width, height) in cars:
    cv2.rectangle(img=car_image, pt1=(x, y), pt2=(x + width, y + height), color=(0, 255, 0), thickness=2)

# Display the Detected Image
cv2.imshow(winname="Detected Car", mat=car_image)
cv2.waitKey()
cv2.destroyAllWindows()
