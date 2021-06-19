import numpy as np
import cv2

# At first read the image
img = cv2.imread(filename="image_example/lena.png")

# Initialize the kernel
kernel = np.ones((5,5), np.uint8)
# print(kernel)
# this the kernel output

# [[1 1 1 1 1]
#  [1 1 1 1 1]
#  [1 1 1 1 1]
#  [1 1 1 1 1]
#  [1 1 1 1 1]]


# 1) Convert into gray image
imgGray = cv2.cvtColor(src=img,code=cv2.COLOR_BGR2GRAY)

# 2) Convert into blur

# src =	input image
# dst = output image
#
# ksize =	Gaussian Kernel Size. [height width]. height and width should be odd and can have different values.
# If ksize is set to [0 0], then ksize is computed from sigma values.
#
# sigmaX = Kernel standard deviation along X-axis (horizontal direction).
# sigmaY = Kernel standard deviation along Y-axis (vertical direction). If sigmaY=0, then sigmaX value is taken for sigmaY
# borderType = Specifies image boundaries while kernel is applied on image borders.
# Possible values are : cv.BORDER_CONSTANT cv.BORDER_REPLICATE cv.BORDER_REFLECT cv.
# BORDER_WRAP cv.BORDER_REFLECT_101 cv.BORDER_TRANSPARENT cv.BORDER_REFLECT101 cv.
# BORDER_DEFAULT cv.BORDER_ISOLATED

imgBlur = cv2.GaussianBlur(src=imgGray,ksize=(11,11),sigmaX=0)

# 3) Convert into canny

# Necessary parameters are:
# image: Source/Input image of n-dimensional array.
# threshold1: It is the High threshold value of intensity gradient.
# threshold2: It is the Low threshold value of intensity gradient.
# Optional parameters are:
# apertureSize: Order of Kernel(matrix) for the Sobel filter. Its default value is (3 x 3),
# and its value should be odd between 3 and 7. It is used for finding image gradients.
# Filter is used for smoothening and sharpening of an image.
# L2gradient: This specifies the equation for finding gradient magnitude.
# L2gradient is of boolean type, and its default value is False.

imgCanny = cv2.Canny(image=img,threshold1=150,threshold2=150)
imgCanny2 = cv2.Canny(image=img,threshold1=150,threshold2=150, apertureSize=5, L2gradient=True)

# 4) Convert into dilation

# The dilate() function takes the following parameters.
#
# image: It is a required parameter and an original image on which we need to perform dilation.
# kernel: It is the required parameter is the matrix with which the image is convolved.
# dst: It is the output image of the same size and type as image src.
# anchor: It is a variable of type integer representing the anchor point and its default value Point is (-1, -1)
# which means that the anchor is at the kernel center.

# borderType: It depicts what kind of border to be added. It is defined by flags like cv2.BORDER_CONSTANT,
# cv2.BORDER_REFLECT, etc.

# iterations: It is an optional parameter that takes several iterations.
# borderValue: It is border value in case of a constant border.

#### iterations remove the thikness from image

imgDilation = cv2.dilate(src=imgCanny,kernel=kernel,iterations=1)

# 5) Convert into eroded

# Parameters:
# src: It is the image which is to be eroded .
# kernel: A structuring element used for erosion. If element = Mat(), a 3 x 3 rectangular structuring element is used.
# Kernel can be created using getStructuringElement.
# dst: It is the output image of the same size and type as src.
# anchor: It is a variable of type integer representing anchor point and
# it’s default value Point is (-1, -1) which means that the anchor is at the kernel center.
# borderType: It depicts what kind of border to be added. It is defined by flags like cv2.BORDER_CONSTANT,
# cv2.BORDER_REFLECT, etc.
# iterations: It is number of times erosion is applied.
# borderValue: It is border value in case of a constant border.
# Return Value: It returns an image.

imgErod = cv2.erode(src=imgDilation,kernel=kernel,iterations=1)

# Display all the Images

cv2.imshow(winname="Original Image",mat=img)
cv2.imshow(winname="Gray Scale Image", mat=imgGray)
cv2.imshow(winname="Blur Scale Image", mat=imgBlur)
cv2.imshow(winname="Canny Scale Image", mat=imgCanny)
cv2.imshow(winname="Canny Scale Image2", mat=imgCanny2)
cv2.imshow(winname="Dilation Scale Image", mat=imgDilation)
cv2.imshow(winname="Eroded Scale Image", mat=imgErod)
cv2.waitKey()
cv2.destroyAllWindows()