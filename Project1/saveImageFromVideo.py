import cv2
import os

# Make a directory
# os.mkdir(path="video_to_image")
os.makedirs(name="video_to_image", exist_ok=True)
video_cap = cv2.VideoCapture("Video/video4.mp4")

image_count = 1

while video_cap.isOpened():
    success, frame = video_cap.read()
    if not success:
        print("Unable to read frame")
        break

    is_image_write = cv2.imwrite(filename=f"video_to_image\image{image_count}.jpg", img=frame)
    if is_image_write:
        print(f"Image save at video_to_image\image{image_count}.jpg")

    cv2.imshow(winname="Video", mat=frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    image_count += 1

video_cap.release()
cv2.destroyAllWindows()
