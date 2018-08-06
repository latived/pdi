#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by lativ on 31/07/18 at 13:35
"""

import cv2 as cv
import numpy as np

def doNothing(x):
    pass


def scaleImage2_uchar(src):
    tmp = np.copy(src)
    if src.dtype != np.float32:
        tmp = np.float32(tmp)
    cv.normalize(tmp, tmp, 1, 0, cv.NORM_MINMAX)
    tmp = 255 * tmp
    tmp = np.uint8(tmp)
    return tmp


def createWhiteDisk2(height=100, width=100, xc=50, yc=50, rc=20):
    xx, yy = np.meshgrid(range(height), range(width))
    img = np.array(
        ((xx - xc) ** 2 + (yy - yc) ** 2 - rc ** 2) < 0).astype('float64')
    return img

def applyLogTransform(img):
    img2 = np.copy(img)
    img2 += 1
    img2 = np.log(img2)
    return img2


cv.namedWindow("img", cv.WINDOW_KEEPRATIO)
cv.namedWindow("mask", cv.WINDOW_KEEPRATIO)

img = cv.imread('../img/lena_noise.jpg', cv.IMREAD_GRAYSCALE)
img = np.float32(img)
img = img / 255.0

rows = img.shape[0]
cols = img.shape[1]

freq = 90
theta = 10
gain = 30

cv.createTrackbar("Freq", "img", freq, 500, doNothing)
cv.createTrackbar("Theta", "img", theta, 100, doNothing)
cv.createTrackbar("Gain", "img", gain, 100, doNothing)

bandwidth = 2
outer_radius = 256 - 210 + bandwidth
inner_radius = 256 - 210 - bandwidth
cv.createTrackbar("in_radius", "mask", inner_radius, img.shape[1], doNothing)
cv.createTrackbar("out_radius", "mask", outer_radius, img.shape[1], doNothing)

while cv.waitKey(1) != ord('q'):
    outer_radius = cv.getTrackbarPos("in_radius", "mask")
    inner_radius = cv.getTrackbarPos("out_radius", "mask")

    mask = 1 - (createWhiteDisk2(rows, cols, int(cols / 2),
                                 int(rows / 2), outer_radius) - createWhiteDisk2(rows, cols, int(cols / 2),
                                                                                 int(rows / 2), inner_radius))

    planes = [np.zeros(img.shape, dtype=np.float64),
              np.zeros(img.shape, dtype=np.float64)]

    planes[0][:] = np.float64(img[:])
    planes[1][:] = np.float64(img[:])

    img2 = cv.merge(planes)
    img2 = cv.dft(img2)
    planes = cv.split(img2)
    mag = cv.magnitude(planes[0], planes[1])
    mag = applyLogTransform(mag)
    planes[0] = np.multiply(np.fft.fftshift(mask), planes[0])
    planes[1] = np.multiply(np.fft.fftshift(mask), planes[1])
    tmp = cv.merge(planes)
    tmp = cv.idft(tmp)


    cv.imshow("mag", cv.applyColorMap(np.fft.fftshift(scaleImage2_uchar(mag)), cv.COLORMAP_OCEAN))
    cv.imshow("mask", scaleImage2_uchar(mask))
    cv.imshow("tmp", scaleImage2_uchar(tmp[:, :, 0]))

cv.destroyAllWindows()
