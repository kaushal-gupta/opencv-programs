import cv2
import numpy as np

img =cv2.imread('sanmarcos.jpg')
height,width=img.shape[:2]

start_row,start_col=int(height*0.25),int(width*0.25)
end_row,end_col=int(height*0.75),int(width*0.75)

cropped=img[start_row:end_row,start_col:end_col]

cv2.imshow("orginal" ,img)
cv2.imshow("cropped",cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()
