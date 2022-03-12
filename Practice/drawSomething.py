import cv2
import numpy as np

# Create an RGB image
myimg = np.zeros((612,612,3), np.uint8)

print(myimg)
print(f"Number of shape: {myimg.shape}")
print(f"Number of dim: {myimg.ndim}")

# Draw a line
### Parameters:
    # 1) img = simple that we are read
    # 2) pt1 = means starting point of the line. pt1=(width or x, height or y)
    # 3) pt2 = means ending point of the line. pt2=(width or x2, height or y2)
    # 4) color = this is simple color
    # 5) thickness = means the lines conditions. line should fat or thick
cv2.line(img=myimg, pt1=(0,0), pt2=(myimg.shape[1], myimg.shape[0]), color=(255,255,255), thickness=3)

# Draw a rectangle

### Parameters:
    # 1) img = simple that we are read
    # 2) pt1 = means starting point of the line. pt1=(width or x, height or y)
    # 3) pt2 = means ending point of the line. pt2=(width or x2, height or y2)
    # 4) color = this is simple color
    # 5) thickness = means the lines conditions. line should fat or thick
cv2.rectangle(img=myimg, pt1=(0,0), pt2=(250,350), color=(0,0,255), thickness=2)

# Draw a circle

### Parameters:
    # 1) img = simple that we are read
    # 2) center = center=(width, height)
    # 3) redius = distance from the center of the circle
    # 4) color = this is simple color
    # 5) thickness = means the lines conditions. line should fat or thick
cv2.circle(img=myimg, center=(400,100), radius=50, color=(0,255,255), thickness=4)
cv2.circle(img=myimg, center=(500,100), radius=50, color=(0,255,255), thickness=cv2.FILLED)

# PutText

# Parameters:
# image: It is the image on which text is to be drawn.
# text: Text string to be drawn.
# org: It is the coordinates of the bottom-left corner of the text string in the image.
# The coordinates are represented as tuples of two values i.e. (X coordinate value, Y coordinate value).

# font: It denotes the font type. Some of font types are FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN, , etc.
# fontScale: Font scale factor that is multiplied by the font-specific base size.
# color: It is the color of text string to be drawn. For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.
# thickness: It is the thickness of the line in px.
# lineType: This is an optional parameter.It gives the type of the line to be used. Type of line, whether 8-connected, anti-aliased line etc.
# By default, it is 8-connected. cv.LINE_AA gives anti-aliased line which looks great for curves.
# cv::FILLED = -1, cv::LINE_4 = 4, cv::LINE_8 = 8, cv::LINE_AA = 16
# bottomLeftOrigin: This is an optional parameter.
# When it is true, the image data origin is at the bottom-left corner. Otherwise, it is at the top-left corner.

cv2.putText(img=myimg, text=" OPEN CV ", org=(300,200),
            fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1,color=(255,0,255),thickness=1)

# Show the image
cv2.imshow("Image", myimg)
cv2.waitKey()
cv2.destroyAllWindows()
