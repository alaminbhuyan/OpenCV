import cv2
import numpy as np


# Different Image in multiple time in the same window
img = cv2.imread(filename="image_example/lena.png")
img = cv2.resize(src=img, dsize=(300, 300))

img2 = cv2.imread(filename="image_example/multipleFace1.jpg")
img2 = cv2.resize(src=img2, dsize=(300, 300))

img3 = cv2.imread(filename="image_example/alamin2.jpg")
img3 = cv2.resize(src=img3, dsize=(300, 300))


img4 = np.hstack((img2, img, img3))
img5 = np.vstack((img4, img4, img4))

cv2.imshow(winname="Multiple Image in single window", mat=img5)
cv2.waitKey()
cv2.destroyAllWindows()