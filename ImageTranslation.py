import cv2
import numpy as np
img = cv2.imread('sanmarcos.jpg')
height,width=img.shape[:2]
print(height)
print(width)
quater_height,quater_width=height/4,width/4
print(quater_height)
print(quater_width)

T=np.float32([[1,0,quater_width],
             [0,1,quater_height]])

print(T)

img_translation=cv2.warpAffine(img,T,(width,height))
cv2.imshow("orignal image",img)
cv2.imshow("Traslation",img_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()
