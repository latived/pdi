#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by lativ on 22/08/18 at 23:43
"""
# %% Importing modules

from dip import *

# %% Basic vars

exam_folder = '/home/lativ/Documents/UFAL/repos/pdi/lista_prova2/'


# %% Test

img = cv2.imread(exam_folder + '1.png')

cv2.imshow('img', img)
close_windows()

