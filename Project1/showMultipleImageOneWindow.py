import cv2
import numpy as np


# Same Image in multiple time in the same window
img = cv2.imread(filename="image_example/lena.png")
img = cv2.resize(src=img, dsize=(300, 300))

# img2 = np.hstack((img, img, img))
# img3 = np.vstack((img2, img2, img2))

img2 = np.hstack((img, img))
img3 = np.vstack((img2, img2))

cv2.imshow(winname="Multiple Image in single window", mat=img3)
cv2.waitKey()
cv2.destroyAllWindows()
