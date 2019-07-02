import cv2

img =cv2.imread("sanmarcos.jpg")
print(img.shape)
print("Height pixel values:",img.shape[0])
print("width pixel values:",img.shape[1])
cv2.waitKey(0)
cv2.destroyAllWindows()
