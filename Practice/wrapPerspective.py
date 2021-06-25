import cv2
import numpy as np

# Read the orginal image
img = cv2.imread(filename="image_example/cards.jpg")

# Initialize the width and height

width, height = 250, 350

# Locate points of the documents or object which you want to transform
pts1 = np.float32([
    [111,219], # top-left
    [287,188], # top-right
    [154,482], # bottom-left
    [352,440]  # bottom-right
])

pts2 = np.float32([
    [0,0],
    [width,0],
    [0,height],
    [width,height]
])
print(pts1.shape)
print(pts2.shape)

# Parameters:
# ->src: Coordinates of quadrangle vertices in the source image.
# ->dst: Coordinates of the corresponding quadrangle vertices in the destination image.

# Apply Perspective Transform Algorithm
matrix = cv2.getPerspectiveTransform(src=pts1, dst=pts2)

# Parameters:
# ->src: Source Image
# ->dst: output image that has the size dsize and the same type as src.
# ->dsize: size of output image

imgOutput = cv2.warpPerspective(src=img, M=matrix, dsize=(width,height))

## show the output images
cv2.imshow(winname="Orginal Card Image", mat=img)
cv2.imshow(winname="Warper Image", mat=imgOutput)

cv2.waitKey()
cv2.destroyAllWindows()
