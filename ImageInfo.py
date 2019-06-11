import cv2

img =cv2.imread("sanmarcos.jpg")
print(img.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()
