import cv2
import numpy

image = cv2.imread("image_examples/elephant.jpg")
cv2.imshow("Test image",image)
cv2.waitKey()
cv2.destroyAllWindows()
print(image.shape)