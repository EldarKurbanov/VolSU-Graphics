import cv2
import numpy

image = cv2.imread('images/lab3.7.in.jpg')
grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
for x in range(1, 100, 20):
    kernel = numpy.ones((x, x), numpy.uint8)
    top_hat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)
    cv2.imwrite("images/lab3.7.out_{}.jpg".format(x), top_hat)
