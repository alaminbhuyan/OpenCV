import cv2


# Load the image

img = cv2.imread(filename="Images/image1.jpg")

# show the image
# cv2.imshow(winname="Real image", mat=img)
# cv2.imshow("Real image", img)

print(type(img))
