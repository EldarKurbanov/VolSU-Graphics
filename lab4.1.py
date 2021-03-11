import numpy
import cv2
image = cv2.imread('images/lab4.1.in.jpg')

srcTri = numpy.array([[0, 0], [image.shape[1] - 1, 0], [0, image.shape[0] - 1]]).astype(numpy.float32)
dstTri = numpy.array([[0, image.shape[1]*0.33], [image.shape[1]*0.85, image.shape[0]*0.25],
                      [image.shape[1]*0.15, image.shape[0]*0.7]]).astype(numpy.float32)

warp_mat = cv2.getAffineTransform(srcTri, dstTri)
warp_dst = cv2.warpAffine(image, warp_mat, (image.shape[1], image.shape[0]))

# rotate image after warp
image_center = (warp_dst.shape[1]//2, warp_dst.shape[0]//2)
image_angle = -50
image_scale = 0.6

rot_mat = cv2.getRotationMatrix2D(image_center, image_angle, image_scale)
warp_rotate_dst = cv2.warpAffine(warp_dst, rot_mat, (warp_dst.shape[1], warp_dst.shape[0]))

cv2.imwrite('images/lab4.1.out.jpg', warp_rotate_dst)
