#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by lativ on 09/08/18 at 15:55
"""
# %% Importing libs
import cv2
import numpy as np

# %% Basic methods

def doNothing():
    pass


def close_windows():
    while True:
        if 0xFF & cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()


def createHolesInImage(img, height, width, xc, yc, rc):
    xx, yy = np.meshgrid(range(height), range(width))
    img = img - np.array(((xx - xc) ** 2 + (yy - yc) ** 2 - rc ** 2) < 0).astype('float64')
    return img

# %% Basic vars
size = 3

# %% Erosion

iterations = 1

cv2.namedWindow('original', cv2.WINDOW_KEEPRATIO)
cv2.namedWindow('morfop', cv2.WINDOW_KEEPRATIO)

cv2.createTrackbar('ks', 'morfop', size, 25, doNothing)
cv2.createTrackbar('iters', 'morfop', iterations, 10, doNothing)

while 0xFF & cv2.waitKey(1) != ord('q'):
    size = cv2.getTrackbarPos('ks', 'morfop')
    iterations = cv2.getTrackbarPos('iters', 'morfop')

    if size < 3:
        size = 3

    img = cv2.imread('j.png', 0)
    kernel = np.ones((size, size), np.uint8)
    erosion = cv2.erode(img, kernel, iterations=iterations)

    cv2.imshow('original', img)
    cv2.imshow('morfop', erosion)

cv2.destroyAllWindows()

# %%  Dilation

iterations = 1

cv2.namedWindow('original', cv2.WINDOW_KEEPRATIO)
cv2.namedWindow('morfop', cv2.WINDOW_KEEPRATIO)

cv2.createTrackbar('ks', 'morfop', size, 25, doNothing)
cv2.createTrackbar('iters', 'morfop', iterations, 10, doNothing)

while 0xFF & cv2.waitKey(1) != ord('q'):
    size = cv2.getTrackbarPos('ks', 'morfop')
    iterations = cv2.getTrackbarPos('iters', 'morfop')

    if size < 3:
        size = 3

    img = cv2.imread('j.png', 0)
    kernel = np.ones((size, size), np.uint8)
    dilate = cv2.dilate(img, kernel, iterations=iterations)

    cv2.imshow('original', img)
    cv2.imshow('morfop', dilate)

cv2.destroyAllWindows()

# %% Opening

cv2.namedWindow('original with noise', cv2.WINDOW_KEEPRATIO)
cv2.namedWindow('morfop', cv2.WINDOW_KEEPRATIO)

cv2.createTrackbar('ks', 'morfop', size, 25, doNothing)

while 0xFF & cv2.waitKey(1) != ord('q'):
    size = cv2.getTrackbarPos('ks', 'morfop')

    if size < 3:
        size = 3

    img = cv2.imread('j.png', 0)
    # Adding noise
    noise = np.zeros(img.shape, img.dtype)
    cv2.randn(noise, 0, 150)
    img =  img + noise
    kernel = np.ones((size, size), np.uint8)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    cv2.imshow('original with noise', img)
    cv2.imshow('morfop', opening)

cv2.destroyAllWindows()

# %% Closing

num_holes = 100
size_hole = 3

cv2.namedWindow('original with holes', cv2.WINDOW_KEEPRATIO)
cv2.namedWindow('morfop', cv2.WINDOW_KEEPRATIO)

cv2.createTrackbar('ks', 'morfop', size, 25, doNothing)
cv2.createTrackbar('num_holes', 'original with holes', num_holes, 500, doNothing)
cv2.createTrackbar('size_hole', 'original with holes', size_hole, 15, doNothing)

while 0xFF & cv2.waitKey(1) != ord('q'):
    size = cv2.getTrackbarPos('ks', 'morfop')
    num_holes = cv2.getTrackbarPos('num_holes', 'original with holes')
    size_hole = cv2.getTrackbarPos('size_hole', 'original with holes')

    if size < 3:
        size = 3

    img = cv2.imread('j.png', 0)

    disk = np.zeros(img.shape, np.float64)

    for _ in range(num_holes):

        # randint 'high' parameter is exclusive, therefore we add 1
        yc = np.random.randint(0, disk.shape[1])
        xc = np.random.randint(0, disk.shape[0])
        rc = np.random.randint(size_hole)

        for x in range(disk.shape[0]):
            for y in range(disk.shape[1]):
                if (x - xc) * (x - xc) + (y - yc) * (y - yc) <= rc * rc:
                    disk[x][y] = 1.0

    # Inserting holes
    cv2.normalize(img, img, 1, 0, cv2.NORM_MINMAX)
    img = img - disk

    kernel = np.ones((size, size), np.uint8)
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('original with holes', img)
    cv2.imshow('morfop', closing)

cv2.destroyAllWindows()
