import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)
 
# Draw a diagonal blue line with thickness of 5 px
cv2.line(img,(0,0),(511,511),(255,0,0),5)

#Drawing Rectangle
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

#Drwaing circle using center coordinates and the radius
cv2.circle(img,(447,63), 63, (0,0,255), -1)

#drwaing the ellipse
cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

#Adding text

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2)

cv2.imshow("Drawing FUnction",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
