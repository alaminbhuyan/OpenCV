
# HSV = H -> Hue or color, S -> Saturation means how pure the color is, V -> Value means how bright the color is
# ********************** For Image this lines of code ************************
import numpy
import cv2
import numpy as np

img = cv2.imread(filename="image_example/lambo.png")
# Let me reshape the img. Image is a little bit large
resizeImg = cv2.resize(src=img,dsize=(500,400))

# Convert img BGR to HSV
imgHSV = cv2.cvtColor(src=resizeImg,code=cv2.COLOR_BGR2HSV)

# Create a function
def empty(x):
    pass

# Create trackbar
cv2.namedWindow(winname="HSV")
cv2.resizeWindow(winname="HSV",width=640,height=240)
# Parameters:
# 1) value = min value 2) count = max value 3) onChange = a method
cv2.createTrackbar("HUE MIN","HSV",0,179,empty)
cv2.createTrackbar("HUE MAX","HSV",179,179,empty)
cv2.createTrackbar("SAT MIN","HSV",0,255,empty)
cv2.createTrackbar("SAT MAX","HSV",255,255,empty)
cv2.createTrackbar("VALUE MIN","HSV",0,255,empty)
cv2.createTrackbar("VALUE MAX","HSV",255,255,empty)

# ************************** createtrackbar() takes no keyword arguments *************************************
# cv2.createTrackbar(trackbarName="HUE MIN",windowName="HSV",value=0,count=179,onChange=empty)
# cv2.createTrackbar(trackbarName="HUE MIN",windowName="HSV",value=179,count=179,onChange=empty)
# cv2.createTrackbar(trackbarName="SAT MIN",windowName="HSV",value=0,count=255,onChange=empty)
# cv2.createTrackbar(trackbarName="SAT MAX",windowName="HSV",value=255,count=255,onChange=empty)
# cv2.createTrackbar(trackbarName="VALUE MIN",windowName="HSV",value=0,count=255,onChange=empty)
# cv2.createTrackbar(trackbarName="VALUE MAX",windowName="HSV",value=255,count=255,onChange=empty)
# ****************************************************************************

while True:
    # Grab the all trackbar values
    # h_min = cv2.getTrackbarPos(trackbarname="HUE MIN",winname="HSV")
    h_min = cv2.getTrackbarPos("HUE MIN","HSV")
    print(h_min)


    # Stack the image
    stackImg = np.hstack([resizeImg,imgHSV])

    # cv2.imshow(winname="Original Image", mat=resizeImg)
    # cv2.imshow(winname="HSV Image", mat=imgHSV)
    cv2.imshow(winname="HSV Image", mat=stackImg)
    cv2.waitKey()



# ********************** For Webcam this lines of code ************************

# import cv2
# import numpy
#
# frameWidth = 640
# frameHeight = 480
# cap = cv2.VideoCapture(1)
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)
#
# def empty(a):
#     pass
#
# cv2.namedWindow("HSV")
# cv2.resizeWindow("HSV",640,240)
# cv2.createTrackbar("HUE Min","HSV",0,179,empty)
# cv2.createTrackbar("HUE Max","HSV",179,179,empty)
# cv2.createTrackbar("SAT Min","HSV",0,255,empty)
# cv2.createTrackbar("SAT Max","HSV",255,255,empty)
# cv2.createTrackbar("VALUE Min","HSV",0,255,empty)
# cv2.createTrackbar("VALUE Max","HSV",255,255,empty)
#
# while True:
#
#     _, img = cap.read()
#     imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#
#     h_min = cv2.getTrackbarPos("HUE Min","HSV")
#     h_max = cv2.getTrackbarPos("HUE Max", "HSV")
#     s_min = cv2.getTrackbarPos("SAT Min", "HSV")
#     s_max = cv2.getTrackbarPos("SAT Max", "HSV")
#     v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
#     v_max = cv2.getTrackbarPos("VALUE Max", "HSV")
#     print(h_min)
#
#     lower = np.array([h_min,s_min,v_min])
#     upper = np.array([h_max,s_max,v_max])
#     mask = cv2.inRange(imgHsv,lower,upper)
#     result = cv2.bitwise_and(img,img, mask = mask)
#
#     mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
#     hStack = np.hstack([img,mask,result])
#     #cv2.imshow('Original', img)
#     #cv2.imshow('HSV Color Space', imgHsv)
#     #cv2.imshow('Mask', mask)
#     #cv2.imshow('Result', result)
#     cv2.imshow('Horizontal Stacking', hStack)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
