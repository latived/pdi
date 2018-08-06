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

def createWhiteDisk(height=100, width=100, xc=50, yc=50, rc=20):
    xx, yy = np.meshgrid(range(height), range(width))
    img = np.array(
        ((xx - xc) ** 2 + (yy - yc) ** 2 - rc ** 2) < 0).astype('float64')
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

size = 500

disk = np.zeros((size, size), np.float64)

for _ in range(30):

    # randint 'high' parameter is exclusive, therefore we add 1
    yc = np.random.randint(0, size+1)
    xc = np.random.randint(0, size+1)
    rc = np.random.randint(10, 31)

    for x in range(disk.shape[0]):
        for y in range(disk.shape[1]):
            if (x - xc) * (x - xc) + (y - yc) * (y - yc) <= rc * rc:
                disk[x][y] = 1.0

cv2.imshow('disk', disk)

while True:
    if 0xFF & cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()




