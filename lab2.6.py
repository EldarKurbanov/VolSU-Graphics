import cv2

image = cv2.imread('images/lab2.6.in.jpg')
gaussSmoothImage = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imwrite('images/lab2.6.out.jpg', gaussSmoothImage)
