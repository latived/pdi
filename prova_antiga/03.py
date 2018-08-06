#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by lativ on 31/07/18 at 14:27
"""
import cv2
import numpy as np

cv2.namedWindow('img', cv2.WINDOW_KEEPRATIO)
cv2.namedWindow('img2', cv2.WINDOW_KEEPRATIO)

img = cv2.imread('coded_message.png', cv2.IMREAD_GRAYSCALE)
img2 = np.copy(img)

slice = 0

img2 = cv2.bitwise_and(img, 1 << slice, img2)

img2 = np.asarray(img2, np.float32)

cv2.normalize(img2, img2, 0, 1, cv2.NORM_MINMAX)

cv2.imshow('img', img)
cv2.imshow('img2', img2)

while True:
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()


