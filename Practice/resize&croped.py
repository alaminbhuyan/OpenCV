import cv2
import numpy as np

# Read the image
img = cv2.imread(filename="image_example/lambo.png")
print(img.shape)

# Resizing the image
# dsize = (width, height)

imgResize = cv2.resize(src=img,dsize=(300,200))
print(imgResize.shape)

# Image cropped

# 0:200 --> height, 200:500 --> width

imgCropped = img[0:200,200:500]
print(imgCropped.shape)


# Shows all image window

cv2.imshow("Original Image", img)
cv2.imshow("Resize Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)

cv2.waitKey()
cv2.destroyAllWindows()