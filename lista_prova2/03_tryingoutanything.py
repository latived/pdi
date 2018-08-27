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

# %% 1) Drawing a circle

rows = 500
cols = 500
radius = 200

img = createWhiteDisk2(rows, cols, rows/2, cols/2, radius)

cv2.imshow('whiteDisk', img)
close_windows()

# %% Drawing a simple square with colors from red to red, as in 3.png

rows = 600
cols = 600

blue = np.zeros((rows, cols), dtype=np.uint8)
green = np.copy(blue)
red = np.copy(blue)

limit = rows // 6

for r in range(0, rows):
    # Red
    for c in range(0, limit):
        red[r, c] = 255

    # Yellow
    for c in range(limit, 2*limit):
        red[r, c] = 255
        green[r, c] = 255

    # Green
    for c in range(2*limit, 3*limit):
        green[r, c] = 255

    # Cyan
    for c in range(3*limit, 4*limit):
        green[r, c] = 255
        blue[r, c] = 255

    # Blue
    for c in range(4*limit, 5*limit):
        blue[r, c] = 255

    # Magenta
    for c in range(5*limit, cols):
        blue[r, c] = 255
        red[r, c] = 255

bgr = [blue, green, red]
bgr = cv2.merge(bgr)

cv2.imshow('hsv colors from red to magenta in a square', bgr)
close_windows()

# %% Cropping a circle in the square

circle = createWhiteDisk(rows, cols, rows//2, cols//2, radius)

blue = np.multiply(blue, circle)
green = np.multiply(green, circle)
red = np.multiply(red, circle)

bgr = [blue, green, red]
bgr = cv2.merge(bgr)

cv2.imshow('Cropped square', bgr)
close_windows()

# %% hsv colors with degrade

rows = 600
cols = 600

blue = np.zeros((rows, cols), dtype=np.uint8)
green = np.copy(blue)
red = np.copy(blue)

limit = rows // 6

for r in range(0, rows):

    # value * (c+1)/limit

    # Red
    for c in range(0, limit):
        red[r, c] = 255
        green[r, c] = 255 * (c + 1)/limit

    # Yellow
    for c in range(0, limit):
        red[r, c + limit] = 255 - (255 * c/limit)
        green[r, c + limit] = 255

    # Green
    for c in range(0, limit):
        green[r, c + limit*2] = 255
        blue[r, c + limit*2] = 255 * (c + 1)/limit

    # Cyan
    for c in range(0, limit):
        green[r, c + limit*3] = 255 - (255 * c/limit)
        blue[r, c + limit*3] = 255

    # Blue
    for c in range(0, limit):
        blue[r, c + limit*4] = 255
        red[r, c + limit*4] = 255 * (c + 1)/limit

    # Magenta
    for c in range(0, limit):
        blue[r, c + limit*5] = 255 - (255 * c/limit)
        red[r, c + limit*5] = 255

bgr = [blue, green, red]
bgr = cv2.merge(bgr)

cv2.imshow('hsv colors from red to magenta in a square with a nice degrade', bgr)
close_windows()


# %% A red square with added white at the edges


r_square = 255 * np.ones((rows, cols), np.uint8)
g_square = np.zeros((rows, cols), np.uint8)
b_square = np.zeros((rows, cols), np.uint8)

xc, yc = rows//2, cols//2

white_factor = 127
avg_max_dist = np.mean([euclidean_dist((xc, yc), (0, 0)),
                    euclidean_dist((xc, yc), (0, cols - 1)),
                    euclidean_dist((xc, yc), (rows - 1, cols - 1)),
                    euclidean_dist((xc, yc), (rows - 1, 0))])

for r in range(rows):
    for c in range(cols):
        h = np.square(xc - r) + np.square(yc - c)
        h = np.sqrt(h)

        prop = h/avg_max_dist

        # If I invert and put (1 - prop), it will create a white disk at the center
        g_square[r, c] = prop * white_factor
        b_square[r, c] = prop * white_factor


img = [b_square, g_square, r_square]
img = cv2.merge(img)

cv2.imshow('red with white degrade, I think', img)
close_windows()

