import cv2
import numpy as np
img = cv2.imread('sanmarcos.jpg')
rotated_img=cv2.transpose(img)
cv2.imshow("rotated",rotated_img)
cv2.imshow("orginal",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
