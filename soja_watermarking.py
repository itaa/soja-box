#!/usr/bin/env python3


import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


# 读取图片
img = Image.open('./imgs/gl1.jpg')
mark = Image.open('./imgs/watermark.jpg')
fig = plt.figure('原图')
img_fig = fig.add_subplot(1, 1, 1)
plt.imshow(img)
plt.show()


def generate_random_list(img):
    h = img.height
    w = img.width
    h_list = list(range(h))
    w_list = list(range(w))
    np.random.shuffle(h_list)
    np.random.shuffle(w_list)
    return h_list, w_list


