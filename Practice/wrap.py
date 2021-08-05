import cv2
import numpy as np

# Read the original image
img = cv2.imread(filename="image_example/cards.jpg")

pts1 = np.float32([
    [111,219], # top-left
    [287,188], # top-right
    [154,482], # bottom-left
    [352,440]  # bottom-right
])
print(pts1)

for x in range(0,4):
    cv2.circle(img=img, center=(int(pts1[x][0]),int(pts1[x][1])), radius=5,color=(0,0,255), thickness=cv2.FILLED)

cv2.imshow("Orginal Image", img)
cv2.waitKey()
cv2.destroyAllWindows()