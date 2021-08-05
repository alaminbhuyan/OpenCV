
# **************************** Basic detecting *****************************************

# import numpy as np
# import cv2
#
# def mousePoints(event, x, y, flags, params):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(x, y)
#
# img = cv2.imread("image_example/cards.jpg")
#
# cv2.imshow("Original Image", img)
# cv2.setMouseCallback("Original Image", mousePoints)
# cv2.waitKey()
# cv2.destroyAllWindows()
# **************************** WARP PRESPECTIVE IMPLEMANTAION WITH MOUSE CLICKS ***************************

import cv2
import numpy as np

circles = np.zeros((4,2), dtype=int)
counter = 0

def mousePoints(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x, y
        counter = counter + 1
        print(circles)

img = cv2.imread(filename="image_example/book.jpg")
resizeImg = cv2.resize(src=img, dsize=(700,700))
while True:
    if counter == 4:
        width, height = 350, 450
        pts1 = np.float32([
            circles[0], # top-left
            circles[1], # top-right
            circles[2], # bottom-left
            circles[3]  # bottom-right
        ])
        pts2 = np.float32([
            [0,0],
            [width,0],
            [0,height],
            [width,height]
        ])
        matrix = cv2.getPerspectiveTransform(src=pts1, dst=pts2)
        imgOutput = cv2.warpPerspective(src=resizeImg, M=matrix, dsize=(width,height))
        cv2.imshow(winname="Warper Image", mat=imgOutput)


    for x in range(0,4):
        cv2.circle(img=resizeImg, center=(int(circles[x][0]),int(circles[x][1])), radius=3,color=(0,0,255), thickness=cv2.FILLED)


    ## show the output images
    cv2.imshow(winname="Original Image", mat=resizeImg)
    # cv2.setMouseCallback("Original Image", mousePoints)
    cv2.setMouseCallback(window_name="Original Image", on_mouse=mousePoints)
    cv2.waitKey(1)
