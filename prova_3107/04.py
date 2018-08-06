#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by lativ on 31/07/18 at 15:26
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

folder = '2018_1_AB1'
# %% Define functions
def doNothing(x):
    pass


def create2DGaussian(rows=60,
                     cols=60,
                     mx=30,
                     my=30,
                     sx=5,
                     sy=50,
                     theta=0):
    xx0, yy0 = np.meshgrid(range(rows), range(cols))
    xx0 -= mx
    yy0 -= my
    theta = np.deg2rad(theta)
    xx = xx0 * np.cos(theta) - yy0 * np.sin(theta)
    yy = xx0 * np.sin(theta) + yy0 * np.cos(theta)
    try:
        img = np.exp(- ((xx ** 2) / (2 * sx ** 2) +
                        (yy ** 2) / (2 * sy ** 2)))
    except ZeroDivisionError:
        img = np.zeros((rows, cols), dtype='float64')

    cv2.normalize(img, img, 1, 0, cv2.NORM_MINMAX)
    return img


def scaleImage2_uchar(src):
    tmp = np.copy(src)
    if src.dtype != np.float32:
        tmp = np.float32(tmp)
    cv2.normalize(tmp, tmp, 1, 0, cv2.NORM_MINMAX)
    tmp = 255 * tmp
    tmp = np.uint8(tmp)
    return tmp


# %%

img = cv2.imread(folder + '/messi.jpg', cv2.IMREAD_COLOR)

rows = 60
cols =  60
theta = 0
xc = 1
yc = 1
sx = 1
sy = 1

cv2.namedWindow('img', cv2.WINDOW_KEEPRATIO)

cv2.createTrackbar("xc", "img", xc, int(rows), doNothing)
cv2.createTrackbar("yc", "img", yc, int(cols), doNothing)
cv2.createTrackbar("sx", "img", sx, int(rows), doNothing)
cv2.createTrackbar("sy", "img", sy, int(cols), doNothing)
cv2.createTrackbar("theta", "img", theta, 360, doNothing)

while 0xFF & cv2.waitKey(1) != ord('q'):
    xc = cv2.getTrackbarPos("xc", "img")
    yc = cv2.getTrackbarPos("yc", "img")
    sx = cv2.getTrackbarPos("sx", "img")
    sy = cv2.getTrackbarPos("sy", "img")
    theta = cv2.getTrackbarPos("theta", "img")

    mask = create2DGaussian(rows, cols, xc, yc, sx, sy, theta)

    img = np.float32(img)
    img2 = cv2.filter2D(img, -1, mask, cv2.BORDER_DEFAULT)

    cv2.imshow("img", scaleImage2_uchar(img2))

cv2.destroyAllWindows()

