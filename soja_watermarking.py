#!/usr/bin/env python3


import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2


# 生成随机序列，用来打散mark，同时也加密了mark
def generate_random_list(image):
    h = image.height
    w = image.width
    h_list = list(range(h // 2))
    w_list = list(range(w))
    np.random.shuffle(h_list)
    np.random.shuffle(w_list)
    return h_list, w_list


def image_to_array(image):
    """
    图片文件转为np数组
    :param image: 图片的文件名
    :return: 转换后的np一维数组
    """
    # 读取图片的大小
    img_long = image.height * image.width
    # rgb通道分离
    r, g, b = image.split()
    r_arr = np.array(r).reshape(img_long) / 255
    g_arr = np.array(g).reshape(img_long) / 255
    b_arr = np.array(b).reshape(img_long) / 255
    # 连结
    result = np.concatenate((r_arr, g_arr, b_arr))
    return result


def image_to_matrix(image):
    """
    图片文件转为np矩阵
    :param image: 图片的文件名
    :return: 转换后的np矩阵
    """
    # 读取图片的宽高
    width, height = image.size
    r, g, b = image.split()
    image_data = image.getdata()
    image_data = np.matrix(image_data, dtype='float32') / 255.0
    result = np.reshape(image_data, (height, width, 3))
    return result


alpha = 1.0
# 读取图片image_dataimage_data
# img = Image.open('./imgs/gl1.jpg')
# mark = Image.open('./imgs/watermark.jpg')
# fig = plt.figure('原图')
# img_fig = fig.add_subplot(1, 1, 1)
# plt.imshow(img)
# plt.show()

img_arr = cv2.imread('./imgs/gl1.jpg')
mark_arr_init = cv2.imread('./imgs/gl1.jpg')

# img_arr = np.asarray(img, dtype="float32") / 255
img_shape = img_arr.shape
mark_shape = (img_shape[0] // 2, img_shape[1], img_shape[2])
# mark_arr_init = np.asarray(mark, dtype="float32") / 255
mark_arr = np.zeros(mark_shape, dtype="float32")
mini_h = min(mark_shape[0], mark_arr_init.shape[0])
mini_w = min(mark_shape[1], mark_arr_init.shape[1])
mark_arr[:mini_h, :mini_w, :] = mark_arr_init[:mini_h, :mini_w, :]

mark_en_h = np.zeros(mark_shape, dtype="float32")
mark_en_l = mark_en_h.copy()
mark_height_list = list(range(img_shape[0]//2))
np.random.shuffle(mark_height_list)
mark_width_list = list(range(img_shape[1]))
np.random.shuffle(mark_width_list)

# encode mark
for i in range(len(mark_height_list)):
    mi = mark_height_list[i]
    for j in range(len(mark_width_list)):
        mj = mark_width_list[j]
        mark_en_h[i, j, :] = mark_arr[mi, mj, :]

# set to mark_encoded
mark_encoded = np.zeros(img_shape, dtype="float32")
mark_encoded[:mark_shape[0], :mark_shape[1], :] = mark_en_h
# symmetric 设置对称部分
for i in range(len(mark_height_list)):
    for j in range(len(mark_width_list)):
        mark_encoded[img_shape[0] - i - 1, img_shape[1] - j - 1, :] = mark_en_h[i, j, :]

# 加 watermark
# f_img_arr 是 img 的频域
f_img_arr = np.fft.fft2(img_arr)
# f_out_img_arr 输出img的频域 ： f_img_arr + mark_encoded
f_out_img_arr = f_img_arr + alpha * mark_encoded
# fft 逆变换，输出空域的img arr
out_img_arr = abs(np.fft.ifft2(f_out_img_arr))

# write to file
cv2.imwrite('./imgs/encode_mark_img.jpg', out_img_arr)



