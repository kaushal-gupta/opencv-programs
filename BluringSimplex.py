import cv2
import numpy as np

img =cv2.imread('sanmarcos.jpg')
cv2.imshow("Orginal Image",img)
cv2.waitKey()

kernel_3x3=np.ones((3,3),np.float32)/7

blurred=cv2.filter2D(img,3,kernel_3x3)
cv2.imshow("3 X 3 kernel blurring",blurred)
cv2.waitKey(0)

kernel_7x7=np.ones((7,7),np.float32)/49
blurred2=cv2.filter2D(img,-1,kernel_7x7)
cv2.imshow("7 X 7 kernel blurring",blurred2)
cv2.waitKey(0)

cv2.destroyAllWindows()
