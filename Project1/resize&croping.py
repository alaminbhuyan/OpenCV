import cv2
import numpy as np

img = cv2.imread("image_examples/lambo.png")
print(img.shape)

# Resizing the image
imgResize = cv2.resize(src=img,dsize=(300,200)) # width 300 height 200
print(imgResize.shape)

# Cropped img
# 0:200 height
#200:500 width
imgCropped = img[0:200,200:500]

cv2.imshow("Orginal image",img)
#cv2.imshow("Resize image",imgResize)
cv2.imshow("Cropped image",imgCropped)
cv2.waitKey(0)
cv2.destroyAllWindows()