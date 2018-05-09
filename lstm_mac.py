# coding=utf-8
from __future__ import print_function
import os
import cv2 as cv
import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

img = np.zeros((256, 256, 3), np.uint8)
cv.line(img, (0, 0), (255, 255), (0, 0, 255), 3)
plt.imshow(img)
plt.title('Test chinese, nest is: 中文')
plt.show()
print(img)



