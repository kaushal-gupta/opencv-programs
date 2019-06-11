import cv2
import numpy as np

img =cv2.imread("sanmarcos.jpg")
cv2.imshow("orginal Image",img)
cv2.waitKey(0)

kernel_sharpening=np.array([[-1,-1,-1,-1,-1],
                            [-1,-1,-1,-1,-1],
                            [-1,-1,25,-1,-1],
                            [-1,-1,-1,-1,-1],
                            [-1,-1,-1,-1,-1]])

sharpned=cv2.filter2D(img,-1,kernel_sharpening)
cv2.imshow("image sharpened",sharpned)
cv2.waitKey(0)
cv2.destroyAllWindows()
