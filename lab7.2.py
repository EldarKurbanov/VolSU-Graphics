import numpy
import cv2
image = cv2.imread('images/lab7.2.in.jpg')

bgr_planes = cv2.split(image)
histSize = 256
histRange = (0, 256)
accumulate = False

b_hist = cv2.calcHist(bgr_planes, [0], None, [histSize], histRange, accumulate=accumulate)
g_hist = cv2.calcHist(bgr_planes, [1], None, [histSize], histRange, accumulate=accumulate)
r_hist = cv2.calcHist(bgr_planes, [2], None, [histSize], histRange, accumulate=accumulate)

hist_w = 512
hist_h = 400
bin_w = int(round(hist_w / histSize))
histImage = numpy.zeros((hist_h, hist_w, 3), dtype=numpy.uint8)

cv2.normalize(b_hist, b_hist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)
cv2.normalize(g_hist, g_hist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)
cv2.normalize(r_hist, r_hist, alpha=0, beta=hist_h, norm_type=cv2.NORM_MINMAX)

for i in range(1, histSize):
    cv2.line(histImage, (bin_w * (i - 1), hist_h - int(b_hist[i - 1])),
             (bin_w * i, hist_h - int(b_hist[i])),
             (255, 0, 0), thickness=2)
    cv2.line(histImage, (bin_w * (i - 1), hist_h - int(g_hist[i - 1])),
             (bin_w * i, hist_h - int(g_hist[i])),
             (0, 255, 0), thickness=2)
    cv2.line(histImage, (bin_w * (i - 1), hist_h - int(r_hist[i - 1])),
             (bin_w * i, hist_h - int(r_hist[i])),
             (0, 0, 255), thickness=2)

cv2.imshow('lab7.2', histImage)
cv2.waitKey(0)
cv2.destroyAllWindows()