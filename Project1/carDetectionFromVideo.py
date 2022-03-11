import cv2

# Create car haarcascades object
car_cascades = cv2.CascadeClassifier("Haarcascades/haarcascade_car.xml")

# Capture the video
capture_video = cv2.VideoCapture("Video/Traffic.mp4")

while capture_video.isOpened():
    success, frames = capture_video.read()
    if success == False:
        break
    # Convert into gray
    gray_image = cv2.cvtColor(src=frames, code=cv2.COLOR_BGR2GRAY)
    # Detect the car
    cars = car_cascades.detectMultiScale(image=gray_image, scaleFactor=1.1, minNeighbors=1)
    # Display rectangle
    i = 0
    for (x, y, width, height) in cars:
        if i % 2 == 0:
            cv2.rectangle(img=frames, pt1=(x, y), pt2=(x + width, y + height), color=(0, 255, 0), thickness=2)
            i += 1
        else:
            cv2.rectangle(img=frames, pt1=(x, y), pt2=(x + width, y + height), color=(255, 0, 0), thickness=2)
            i += 1
        # Display Cars
        cv2.imshow(winname="Detected cars", mat=frames)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Relese the VideoCapture object
capture_video.release()
cv2.destroyAllWindows()

# while True:
#     success, frames = capture_video.read()
#     if success == False:
#         break
#     # Convert into gray
#     gray_image = cv2.cvtColor(src=frames, code=cv2.COLOR_BGR2GRAY)
#     # Detect the car
#     cars = car_cascades.detectMultiScale(image=gray_image, scaleFactor=1.1, minNeighbors=1)
#     # Display rectangle
#     i = 0
#     for (x, y, width, height) in cars:
#         if i % 2 == 0:
#             cv2.rectangle(img=frames, pt1=(x, y), pt2=(x + width, y + height), color=(0, 255, 0), thickness=2)
#             i += 1
#         else:
#             cv2.rectangle(img=frames, pt1=(x, y), pt2=(x + width, y + height), color=(255, 0, 0), thickness=2)
#             i += 1
#         # Display Cars
#         cv2.imshow(winname="Detected cars", mat=frames)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Relese the VideoCapture object
# capture_video.release()
# cv2.destroyAllWindows()
