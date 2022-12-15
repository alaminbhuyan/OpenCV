import cv2

capture_video = cv2.VideoCapture(0)
capture_video.set(3, 264)
capture_video.set(4, 380)
img = cv2.imread("Screenshot_1.jpg")

print(img.shape)

while True:
    success, frame = capture_video.read()
    if success:
        # img[100:100 + 300, 55:55 + 540] = frame
        # cv2.imshow("video", img)
        cv2.imshow("video", frame)
        print(frame.shape)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture_video.release()
cv2.destroyAllWindows()
