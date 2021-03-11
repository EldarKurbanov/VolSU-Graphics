import numpy
import math
import cv2

image = cv2.imread('images/lab6.1.in.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_edges = cv2.Canny(image_gray, 50, 150, apertureSize=3)
lines = cv2.HoughLinesP(image_edges, 1, numpy.pi/180, 100, minLineLength=100, maxLineGap=10)
for line in lines:
    x1, y1, x2, y2 = line[0]
    angle = math.atan2(y1 - y2, x1 - x2)
    print(angle * 180 / numpy.pi)
    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
cv2.imshow('lab6.1', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
