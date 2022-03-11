import cv2


class MakeSketchFromVideo:
    def __init__(self):
        self.capture_video = cv2.VideoCapture("Video/video4.mp4")
        # self.capture_video = cv2.VideoCapture(0)q

    def make_sketch(self):
        while True:
            response, frame = self.capture_video.read()
            if response == False:
                break
            # Convert into gray
            image_gray = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)
            # Convert into blur
            image_gray_blur = cv2.GaussianBlur(src=image_gray, ksize=(5, 5), sigmaX=0)
            canny_edges = cv2.Canny(image=image_gray_blur, threshold1=60, threshold2=50)
            cv2.imshow(winname="Live Sketch Drawing", mat=canny_edges)
            # wait for 1 ms for kye 'q' no response then show next image
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # # Release and close all window
        self.capture_video.release()
        cv2.destroyAllWindows()


obj = MakeSketchFromVideo()
obj.make_sketch()
