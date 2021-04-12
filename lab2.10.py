import cv2

image = cv2.imread('images/lab2.10.in.jpg')
grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
result = cv2.adaptiveThreshold(grayScale, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imwrite('images/lab2.10.out.jpg', result)
