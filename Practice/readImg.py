import numpy as np
import cv2

img = cv2.imread(filename="image_example/elephant.jpg")
print(img)
print("This is the image shape: ",img.shape)
print("This is the image dimension: ",img.ndim)
# Let's print each dimension of the image
print('Height of Image:', int(img.shape[0]), 'pixels')
print('Width of Image: ', int(img.shape[1]), 'pixels')
cv2.imshow(winname="Elephant Picture", mat=img)
cv2.waitKey()
cv2.destroyAllWindows()
