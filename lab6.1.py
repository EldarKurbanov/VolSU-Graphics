import numpy
import math
import cv2

image = cv2.imread('images/lab6.1.in.old.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_edges = cv2.Canny(image_gray, 50, 150, apertureSize=3)
lines = cv2.HoughLinesP(image_edges, 1, numpy.pi/180, 100, minLineLength=100, maxLineGap=10)
horizontal_line_sum = 0
horizontal_line_count = 0
vertical_line_sum = 0
vertical_line_count = 0
for line in lines:
    x1, y1, x2, y2 = line[0]
    angleRadian = math.atan2(y1 - y2, x1 - x2)
    angle = angleRadian * 180 / numpy.pi
    if 85 < angle < 95:
        vertical_line_sum += angle
        vertical_line_count += 1
    if -180 < angle < -175 or 0 < angle < 5:
        horizontal_line_sum += angle
        horizontal_line_count += 1
    print(angle)
    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
print(vertical_line_count, vertical_line_sum, horizontal_line_count, horizontal_line_sum)
print(vertical_line_sum / vertical_line_count, horizontal_line_sum / horizontal_line_count)
vertical_line_average = vertical_line_sum / vertical_line_count
image_center = tuple(numpy.array(image.shape[1::-1]) / 2)
if vertical_line_average < 90:
    angle = 90 - vertical_line_average
    angle = -angle
else:
    angle = vertical_line_average - 90
rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
