import cv2
import numpy as np

img =cv2.imread('sanmarcos.jpg')

cv2.imshow("orginal",img)
cv2.waitKey(0)

M=np.ones(img.shape,dtype="uint8")*150
added=cv2.add(img,M)
subtract=cv2.subtract(img,M)
mul=cv2.multiply(img,M)

cv2.imshow("added",added)
cv2.imshow("subtracted",subtract)
cv2.imshow("multily",mul)

cv2.waitKey(0)
cv2.destroyAllWindows()
