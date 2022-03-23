import cv2
import os

images = os.listdir(path="C:\\Users\\alami\\Downloads\\New folder")


try:
    for i, image in enumerate(images):
        color_image = cv2.imread(filename=f"C:\\Users\\alami\\Downloads\\New folder\\{image}")
        height, width = color_image.shape[0], color_image.shape[1]
        if height >= 150 and width >= 150:
            resize_img = cv2.resize(src=color_image, dsize=(150, 150))
            cv2.imwrite(filename=f"C:\\Users\\alami\Downloads\\Resize Images\\image{i+1}.jpg",
                        img=resize_img)
        else:
            continue
except Exception as ex:
    print("The error is: ", ex)
finally:
    print("Image resize done")

