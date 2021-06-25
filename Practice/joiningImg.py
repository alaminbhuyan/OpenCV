import cv2
import numpy as np

# Read Original image
img = cv2.imread(filename="image_example/lena.png")

# Resize the  image for comfortable
imgResize = cv2.resize(src=img,dsize=(300,300))

# Joining with Horizontally
imgHorizontal = np.hstack((imgResize,imgResize))

# Joining with Vertically
imgVertically = np.vstack((imgResize,imgResize))

# Show all image window

cv2.imshow("Original Image", img)
cv2.imshow("Join Horizontal Image", imgHorizontal)
cv2.imshow("Join Vertical Image", imgVertically)
cv2.waitKey()
cv2.destroyAllWindows()

