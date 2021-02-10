import cv2
import numpy as np

img = cv2.imread(filename="image_examples/lena.png")
kernel = np.ones((5,5),np.uint8)
# print(kernel)

# convert into gray
imgGray = cv2.cvtColor(src=img,code=cv2.COLOR_BGR2GRAY)
# convert into blur
imgBlur = cv2.GaussianBlur(src=imgGray,ksize=(9,9),sigmaX=0) # ksize = kernel size
# imgBlur = cv2.GaussianBlur(img,(9,9),0)
# convert into canny
imgCanny = cv2.Canny(image=img,threshold1=150,threshold2=200)
# convert into dialation
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1) # iterations remove the thikness from image
# convert into eroded
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)


# display img
cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)
cv2.destroyAllWindows()