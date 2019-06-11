import cv2
img = cv2.imread('sanmarcos.jpg',0)
cv2.imshow('GrayScale image ', img)

cv2.waitKey(0)
ret,bw=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow("Bianry image",bw)
cv2.waitKey(0)
cv2.destroyAllWindows()
