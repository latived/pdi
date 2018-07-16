import cv2
import matplotlib.pyplot as plt
import numpy as np


def doNothing(x):
    pass

#
# Intensity Transformations - Part I
#

# Image negative
# img = cv2.imread("img/lena.png", cv2.IMREAD_GRAYSCALE)
# cv2.imshow("img", 255 - img)
# cv2.waitKey(0)

# Log transform
# img = cv2.imread("img/spectrum.tif", cv2.IMREAD_GRAYSCALE)
# img2 = np.ones(img.shape, np.float64)
# c = 1
# for x in range(img.shape[0]):
#     for y in range(img.shape[1]):
#         intensity = img[x][y]
#         intensity_new = c * np.log(1 + intensity)
#         img2[x][y] = intensity_new
#
# cv2.normalize(img2, img2, 255, 0, cv2.NORM_MINMAX)
#
# plt.subplot("221"); plt.title("Image 1"); plt.imshow(img, "gray")
# plt.subplot("222"); plt.title("Hist 1"); plt.hist(img.ravel(), 256, [0, 255])
# plt.subplot("223"); plt.title("Image 2"); plt.imshow(img2, "gray")
# plt.subplot("224"); plt.title("Hist 2"); plt.hist(img2.ravel(), 256, [0, 255])
# plt.show()

# Intensity transform
# img = cv2.imread("img/spectrum.tif", cv2.IMREAD_GRAYSCALE)
# img2 = np.ones(img.shape, np.uint8)
#
# cv2.namedWindow("img", cv2.WINDOW_KEEPRATIO)
# cv2.namedWindow("img2", cv2.WINDOW_KEEPRATIO)
#
# n = 0
# cv2.createTrackbar("n", "img2", n, 10, doNothing)
#
# while cv2.waitKey(1) != ord('q'):
#
#     n = cv2.getTrackbarPos("n", "img2")
#
#     for x in range(img.shape[0]):
#         for y in range(img.shape[1]):
#             intensity = img[x][y]
#             intensity_new = np.power(intensity, n)
#             img2[x][y] = intensity_new
#
#     cv2.imshow("img", img)
#     cv2.imshow("img2", img2)


