import cv2
import numpy as np

img =cv2.imread('sanmarcos.jpg')
larger=cv2.pyrUp(img)
smaller=cv2.pyrDown(img)

cv2.imshow('orginal',img)
cv2.imshow('smaller',smaller)
cv2.imshow('larger',larger)

cv2.waitKey(0)
cv2.destroyAllWindows()
