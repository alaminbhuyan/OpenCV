# Opencv Support Below Image file format to read & write(Save):
#
# Windows bitmaps – *.bmp, *.dib (always supported)
# JPEG files – *.jpeg, *.jpg, *.jpe (see the Notes section)
# JPEG 2000 files – *.jp2 (see the Notes section)
# Portable Network Graphics – *.png (see the Notes section)
# Portable image format – *.pbm, *.pgm, *.ppm (always supported)
# Sun rasters – *.sr, *.ras (always supported)
# TIFF files – *.tiff, *.tif (see the Notes section)

import cv2


# At first read the image
img = cv2.imread(filename="Images/girl.jpg")

cv2.imshow(winname="Girl image", mat=img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Convert jpg to png

img_output_path = r"Output_images/girl.png"

response = cv2.imwrite(filename=img_output_path, img=img)

if response:
    print(f"Your Image is save {img_output_path} in this location")
else:
    print("Something is wrong")