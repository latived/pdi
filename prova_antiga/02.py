#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by lativ on 31/07/18 at 14:38
"""
import cv2
import numpy as np


# Image sharpening using the Laplacian operator - Part II

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

def img_sharpening_laplacian():

    cv2.namedWindow("img3", cv2.WINDOW_KEEPRATIO)
    #img = cv2.imread("eye.jpg", cv2.IMREAD_GRAYSCALE)
    img = cv2.imread("eye.jpg", cv2.IMREAD_COLOR)

    img = np.float32(img)

    kernel = [[1.0,  1.0, 1.0],
              [1.0, -8.0, 1.0],
              [1.0,  1.0, 1.0]]
    kernel = np.array(kernel)

    cv2.normalize(img, img, 1, 0, cv2.NORM_MINMAX)

    img2 = cv2.filter2D(img, -1, kernel, cv2.BORDER_DEFAULT)

    factor = 5

    cv2.createTrackbar('factor', "New", factor, 100, doNothing)

    while (cv2.waitKey(1) != ord('q')):
        factor = cv2.getTrackbarPos("factor", "New")
        img3 = img - factor/100 * img2

        cv2.imshow("img", scaleImage2_uchar(img))
        cv2.imshow("img3", scaleImage2_uchar(img3))

    cv2.destroyAllWindows()


if __name__ == '__main__':
    img_sharpening_laplacian()