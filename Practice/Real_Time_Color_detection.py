# HSV = H -> Hue or color, S -> Saturation means how pure the color is, V -> Value means how bright the color is
# opencv-python==4.5.5.64
import cv2
import numpy as np

frameWidth = 370
frameHeight = 450
cap = cv2.VideoCapture(0)

cap.set(propId=3, value=frameWidth)
cap.set(propId=4, value=frameHeight)


def empty(a):
    pass


# Parameters:
# 1) value = min value 2) count = max value 3) onChange = a method

cv2.namedWindow(winname="HSV")
cv2.resizeWindow(winname="HSV", width=640, height=240)
# cv2.createTrackbar(trackbarName="HUE MIN",windowName="HSV",value=0,count=179,onChange=empty)
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
cv2.createTrackbar("VALUE Max", "HSV", 255, 255, empty)

while True:
    success, img = cap.read()
    imgHsv = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2HSV)

    # cv2.getTrackbarPos(trackbarname="HUE Min",winname="HSV")
    h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")
    print(h_min)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(src=imgHsv, lowerb=lower, upperb=upper)
    result = cv2.bitwise_and(src1=img, src2=img, mask=mask)

    mask = cv2.cvtColor(src=mask, code=cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img,mask,result])


    # cv2.imshow(winname='Mask', mat=mask)
    # cv2.imshow(winname='Result', mat=result)
    # cv2.imshow(winname="Original Image", mat=img)
    # cv2.imshow(winname="HSV Image", mat=imgHsv)
    cv2.imshow(winname='Horizontal Stacking', mat=hStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#
cap.release()
cv2.destroyAllWindows()
