import cv2
import math

image = cv2.imread(filename="image_example/angle.jpg")

pointsList = []


def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        size = len(pointsList)
        if size != 0 and size % 3 != 0:
            cv2.line(img=image, pt1=tuple(pointsList[round((size - 1) / 3) * 3]), pt2=(x, y), color=(0, 0, 255),
                     thickness=2)
        cv2.circle(img=image, center=(x, y), radius=3, color=(255, 0, 0), thickness=2, lineType=cv2.FILLED)
        pointsList.append([x, y])
        # print(pointsList)
        # print(x, y)


def gradient(point1, point2):
    return ((point2[1] - point1[1]) / (point2[0] - point1[0]))


def getAngle(pointList):
    point1, point2, point3 = pointList[-3:]
    m1 = gradient(point1, point2)
    m2 = gradient(point1, point3)
    angle_radian = math.atan((m2 - m1) / (1 + (m2 * m1)))
    angle_degree = round(math.degrees(angle_radian))
    cv2.putText(img=image, text=str(angle_degree), org=(point1[0] - 40, point1[1] - 20),
                fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1.5, color=(0, 0, 255), thickness=2)


while True:
    if len(pointsList) % 3 == 0 and len(pointsList) != 0:
        getAngle(pointsList)
    cv2.imshow(winname="Image", mat=image)q
    # cv2.setMouseCallback(windowName="Image", onMouse=mousePoints)
    cv2.setMouseCallback(window_name="Image", on_mouse=mousePoints)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        pointsList = []
        image = cv2.imread(filename="image_example/angle.jpg")
        cv2.destroyAllWindows()

