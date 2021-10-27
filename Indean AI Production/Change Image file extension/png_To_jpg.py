import cv2



# At first read the image
img = cv2.imread(filename="Images/boy.png")
img = cv2.resize(src=img, dsize=(700,700))
cv2.imshow(winname="Boy 1.03 MB", mat=img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Convert image into jpg
img_output_path = r"Output_images/boy.jpg"
response = cv2.imwrite(filename=img_output_path, img=img)

print(f"Your Image is save {img_output_path} in this location") if response else print("Something wrong")