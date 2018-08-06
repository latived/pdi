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

# %%

img = cv2.imread(folder + '/baboon.png', cv2.IMREAD_COLOR)

sd = 1

cv2.namedWindow("noisy", cv2.WINDOW_KEEPRATIO)

cv2.createTrackbar("stdev", "noisy", sd, 100, doNothing)

while cv2.waitKey(1) != ord('q'):
    sd = cv2.getTrackbarPos('stdev', 'noisy')

    if sd == 0:
        sd = 1

    noise = np.zeros(img.shape, img.dtype)
    cv2.randn(noise, 0, sd)
    img_kw_with_sp_noise = img + noise

    img_kw_filtered_mb = cv2.medianBlur(img_kw_with_sp_noise, 5)

    cv2.imshow('img', img_kw_with_sp_noise)
    cv2.imshow('noisy', img_kw_filtered_mb)

cv2.destroyAllWindows()

