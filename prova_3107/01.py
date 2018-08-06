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
# %%
def doNothing(x):
    pass


def scaleImage2_uchar(src):
    tmp = np.copy(src)
    if src.dtype != np.float32:
        tmp = np.float32(tmp)
    cv2.normalize(tmp, tmp, 1, 0, cv2.NORM_MINMAX)
    tmp = 255 * tmp
    tmp = np.uint8(tmp)
    return tmp


def createCosineImage(height, width, freq, theta):
    img = np.zeros((height, width), dtype=np.float64)
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            img[x][y] = np.cos(
                2 * np.pi * freq * (x * np.cos(theta) - y * np.sin(theta)))
    return img


def createLinearImage(height, width, theta):
    img = np.zeros((height, width), dtype=np.float64)
    xx, yy = np.meshgrid(range(height), range(width))
    theta = np.deg2rad(theta)
    rho = (xx * np.cos(theta) - yy * np.sin(theta))
    img[:] = rho[:]
    return img


# %%
rows = 100
cols = 100

freq = 1
theta = 45

cv2.namedWindow("img", cv2.WINDOW_KEEPRATIO)

cv2.createTrackbar("Theta", "img", theta, 360, doNothing)

while cv2.waitKey(1) != ord('q'):
    theta = cv2.getTrackbarPos("Theta", "img")
    img = createLinearImage(rows, cols, theta)
    cv2.imshow("img", scaleImage2_uchar(img))

cv2.destroyAllWindows()

