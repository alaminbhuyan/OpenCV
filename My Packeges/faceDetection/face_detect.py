# opencv-python 4.5.5.64
import cv2
import os
import time


class FaceDetectionFromImage:
    def __init__(self, image=None, scaleFactor=None, minNeighbors=None, flags=None, minSize=None, maxSize=None,
                 design: bool = False, color: tuple | list = (255, 0, 0), rec_color: tuple | list = (255, 0, 0),
                 line_thickness: int = 4,
                 rec_thickness: int = 1, corner_line: int = 25):
        self.image = image
        self.scaleFactor = scaleFactor
        self.minNeighbors = minNeighbors
        self.flags = flags
        self.minSize = minSize
        self.maxSize = maxSize
        self.design = design
        self.color = color
        self.line_thickness = line_thickness
        self.rec_thickness = rec_thickness
        self.rec_color = rec_color
        self.corner_line = corner_line

    # This is private method
    def _designRectangle(self, image, faces):
        for (x, y, width, height) in faces:
            x1, y1 = x + width, y + height
            cv2.rectangle(img=image, pt1=(x, y), pt2=(x + width, y + height), color=self.rec_color,
                          thickness=self.rec_thickness)
            # Top Left  x,y
            cv2.line(img=image, pt1=(x, y), pt2=(x + self.corner_line, y), color=self.color,
                     thickness=self.line_thickness)
            cv2.line(img=image, pt1=(x, y), pt2=(x, y + self.corner_line), color=self.color,
                     thickness=self.line_thickness)
            # Top Right  x1,y
            cv2.line(img=image, pt1=(x1, y), pt2=(x1 - self.corner_line, y), color=self.color,
                     thickness=self.line_thickness)
            cv2.line(img=image, pt1=(x1, y), pt2=(x1, y + self.corner_line), color=self.color,
                     thickness=self.line_thickness)
            # Bottom Left  x,y1
            cv2.line(img=image, pt1=(x, y1), pt2=(x + self.corner_line, y1), color=self.color,
                     thickness=self.line_thickness)
            cv2.line(img=image, pt1=(x, y1), pt2=(x, y1 - self.corner_line), color=self.color,
                     thickness=self.line_thickness)
            # Bottom Right  x1,y1
            cv2.line(img=image, pt1=(x1, y1), pt2=(x1 - self.corner_line, y1), color=self.color,
                     thickness=self.line_thickness)
            cv2.line(img=image, pt1=(x1, y1), pt2=(x1, y1 - self.corner_line), color=self.color,
                     thickness=self.line_thickness)
        return image

    def captureFaceFromImage(self):
        c_path = os.getcwd()
        actual_path = c_path.replace('\\', r'\\')
        actual_path = str(actual_path + r"\\faceDetection\\faceDetect.xml")
        classifier = cv2.CascadeClassifier(actual_path)
        gray_image = cv2.cvtColor(src=self.image, code=cv2.COLOR_BGR2GRAY)
        faces = classifier.detectMultiScale(image=gray_image, scaleFactor=self.scaleFactor,
                                            minNeighbors=self.minNeighbors, flags=self.flags, minSize=self.minSize,
                                            maxSize=self.maxSize)
        if self.design:
            img = self._designRectangle(image=self.image, faces=faces)
            return img
        else:
            for (x, y, width, height) in faces:
                cv2.rectangle(img=self.image, pt1=(x, y), pt2=(x + width, y + height), color=(127, 0, 255), thickness=2)
            return self.image


class FaceDetectionFromWebcam(FaceDetectionFromImage):
    def __init__(self, video=None, image=None, scaleFactor=None, minNeighbors=None, flags=None, minSize=None,
                 maxSize=None,
                 design: bool = False, color: tuple | list = (255, 0, 0), rec_color: tuple | list = (255, 0, 0),
                 line_thickness: int = 4,
                 rec_thickness: int = 1, corner_line: int = 25):

        super(FaceDetectionFromWebcam, self).__init__(image=image, scaleFactor=scaleFactor, minNeighbors=minNeighbors,
                                                      flags=flags, minSize=minSize, maxSize=maxSize, design=design,
                                                      color=color, rec_color=rec_color, line_thickness=line_thickness,
                                                      rec_thickness=rec_thickness, corner_line=corner_line)
        self.video = video


    def captureFaceFromWebcam(self):
        c_path = os.getcwd()
        actual_path = c_path.replace('\\', r'\\')
        actual_path = str(actual_path + r"\\faceDetection\\faceDetect.xml")
        classifier = cv2.CascadeClassifier(actual_path)
        present_time = 0
        while True:
            success, frame = self.video.read()
            if success == True:
                # timer = cv2.getTickCount()
                current_time = time.time()
                fps = 1 / (current_time - present_time)
                present_time = current_time
                gray_img = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)
                # Detect the faces
                faces = classifier.detectMultiScale(image=gray_img, scaleFactor=self.scaleFactor,
                                                    minNeighbors=self.minNeighbors)
                cv2.putText(img=frame, text=f"FPS: {int(fps)}", org=(28, 55), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale=0.8, color=(0, 0, 255), thickness=2)
                # fps2 = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

                if self.design:
                    # img = super()._designRectangle(image=frame, faces=faces)
                    img = self._designRectangle(image=frame, faces=faces)
                    # return img

                    # Display Image
                    cv2.imshow(winname="Face Detect Image", mat=img)  # mat= image matrix
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    for (x, y, width, height) in faces:
                        cv2.rectangle(img=frame, pt1=(x, y), pt2=(x + width, y + height), color=self.rec_color,
                                      thickness=self.rec_thickness)
                        # return frame
                    cv2.imshow(winname="Face Detect Image", mat=frame)  # mat= image matrix
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
            else:
                break



# The cv2.getTickCount() function returns us the count of clock signals that was sent from the reference
# event to the time cv2.getTickCount() function is called. The reference event may be anything such as
# the moment when the computer was turned on

# The cv2.getTickFrequency() function returns the number of clock signals sent in a second, which can
# also be called as getTickFrequency
#
# To calculate the time a block of code takes to execute, we can calculate the number of clock signals
# using cv2.getTickCount() at the beginning and the end of the block of code and divide its difference
# by the frequency, which can be obtained using the cv2.getTickFrequency() function.
#
# In this example, let us try to perform some basic OpenCV manipulations such as converting
# the image to grayscale and drawing a rectangle and find the time taken for its execution.