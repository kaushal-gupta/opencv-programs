import cv2

img = cv2.imread('sanmarcos.jpg')
cv2.imshow('orginal image ', img)
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("hue channel",img_hsv[:,:,0])
cv2.imshow("saturation channel",img_hsv[:,:,1])
cv2.imshow("value channel",img_hsv[:,:,2])
cv2.waitKey(0)
cv2.destroyAllWindows()
