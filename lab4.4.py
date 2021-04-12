import cv2
image = cv2.imread('images/lab4.4.in.jpg')
result = cv2.resize(image, (int(image.shape[0] / 1.25), image.shape[1] * 2), interpolation=cv2.INTER_CUBIC)
cv2.imwrite('images/lab4.4.out.jpg', result)
