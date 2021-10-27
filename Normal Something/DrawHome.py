import cv2
import numpy

myimg = numpy.zeros((612,612,3), dtype= numpy.uint8)

# cv2.namedWindow(winname='output',flags=cv2.WINDOW_AUTOSIZE)
# cv2.namedWindow(winname='output')
# cv2.resizeWindow(winname='output', width=700,height=700)

cv2.line(img=myimg, pt1=(100,150),pt2=(400,150), color=(255,255,255),thickness=2)
cv2.line(img=myimg, pt1=(400,150),pt2=(400,400), color=(255,255,255),thickness=2)
cv2.line(img=myimg, pt1=(400,400),pt2=(180,400), color=(255,255,255),thickness=2)
cv2.line(img=myimg, pt1=(180,400),pt2=(180,270), color=(255,255,255),thickness=2)

cv2.line(img=myimg, pt1=(100,270),pt2=(260,270), color=(255,255,255),thickness=2)
cv2.line(img=myimg, pt1=(100,270),pt2=(100,150), color=(255,255,255),thickness=2)
cv2.line(img=myimg, pt1=(260,270),pt2=(260,150), color=(255,255,255),thickness=2)



cv2.imshow("output",myimg)
cv2.waitKey()