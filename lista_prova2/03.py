#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by lativ on 26/08/18 at 19:39

1. Draw a circle with dip.createWhiteDisk
2. From left, in clockwise order: red, yellow, green, cyan, blue, magenta.
3. Compute the distance from the center: the far, the less saturated (add white).

"""

# %% Importing modules

from dip import *


# %% Defining colors as function of circle coordinates.

def fillColorValues(prop_hue, prop_white, angle):
    white_factor = 127  # Not implemented yet
    r, g, b = 0, 0, 0
    if angle < 60:  # Red
        r = 255
        g = 255 * prop_hue
    elif angle < 120:  # Yellow
        r = 255 - (255 * prop_hue)
        g = 255
    elif angle < 180:  # Green
        g = 255
        b = 255 * prop_hue
    elif angle < 240:  # Cyan
        g = 255 - (255 * prop_hue)
        b = 255
    elif angle < 300:  # Blue
        r = 255 * prop_hue
        b = 255
    elif angle < 360:  # Magenta
        r = 255
        b = 255 - (255 * prop_hue)
    else:
        pass

    r = r + ((255 - r) * prop_white)/2
    g = g + ((255 - g) * prop_white)/2
    b = b + ((255 - b) * prop_white)/2

    r = int(r)
    g = int(g)
    b = int(b)

    return r, g, b


def createHSVDisk(height = 100, width = 100, xc = 50, yc = 50, rc = 20):
    r = np.zeros((height, width), np.uint8)
    g = np.zeros((height, width), np.uint8)
    b = np.zeros((height, width), np.uint8)

    hue = [60, 120, 180, 240, 300, 360]  # red to red
    angles = []
    for x in range(height):
        for y in range(width):
            if (x - xc) * (x - xc) + (y - yc) * (y - yc) <= rc * rc:
                angle, dist = angleAndDistFromCenter((xc, yc), (x, y), rc)
                hue_idx = int(angle/60)

                prop_white = dist/rc
                prop_hue = 1 - (hue[hue_idx] - angle)/60

                angles.append((angle, prop_hue))

                r[x, y], g[x, y], b[x, y] = fillColorValues(prop_hue, prop_white, angle)



    hsv_disk = [b, g, r]
    hsv_disk = cv2.merge(hsv_disk)

    return hsv_disk, angles

rows = 600
cols = 600
radius = 250
img, angles = createHSVDisk(rows, cols, rows//2, cols//2, radius)

# %% Show hsv circle

cv2.namedWindow('img', cv2.WINDOW_KEEPRATIO)
cv2.imshow('img', img)
close_windows()



