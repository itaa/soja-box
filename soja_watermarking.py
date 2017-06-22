#!/usr/bin/env python3
# Create by ChunYing.Jia

import numpy as np
import matplotlib.pyplot as plt
import cv2


def generate_random_list(image_shape):
    """
    生成随机序列，用来打散mark，同时也加密了mark
    :param image_shape:
    :return:
    """
    h_list = list(range(image_shape[0] // 2))
    np.random.shuffle(h_list)
    w_list = list(range(image_shape[1]))
    np.random.shuffle(w_list)
    return h_list, w_list


def shuffle_mark_image(mark_image, original_image, random_tuple):
    """
    通过随机数列打乱 make image
    :param mark_image:
    :param original_image:
    :param random_tuple:
    :return:shuffle_mark:
    """

    origin_shape = original_image.shape
    mark_shape = (origin_shape[0] // 2, origin_shape[1], origin_shape[2])

    # 创建大小合适的mark_image
    fitted_mark_image = np.zeros(mark_shape, dtype="float32")
    mini_h = min(mark_shape[0], mark_image.shape[0])
    mini_w = min(mark_shape[1], mark_image.shape[1])
    fitted_mark_image[:mini_h, :mini_w, :] = mark_image[:mini_h, :mini_w, :]

    # 上半部分mark image 的 shuffle
    half_shuffle_mark = np.zeros(mark_shape, dtype="float32")
    mark_height_list, mark_width_list = random_tuple

    # encode mark
    for i in range(len(mark_height_list)):
        mi = mark_height_list[i]
        for j in range(len(mark_width_list)):
            mj = mark_width_list[j]
            half_shuffle_mark[i, j, :] = fitted_mark_image[mi, mj, :]

    # 上半部分mark image 的 shuffle
    shuffle_mark = np.zeros(origin_shape, dtype="float32")
    shuffle_mark[:mark_shape[0], :mark_shape[1], :] = half_shuffle_mark
    # symmetric 设置对称部分
    for i in range(len(mark_height_list)):
        for j in range(len(mark_width_list)):
            shuffle_mark[origin_shape[0] - i - 1, origin_shape[1] - j - 1, :] = half_shuffle_mark[i, j, :]
    return shuffle_mark


if __name__ == "__main__":
    alpha = 1.0
    img_arr = cv2.imread('./imgs/gl1.jpg')
    mark_arr = cv2.imread('./imgs/pnrmark.png')

    random_list_tuple = generate_random_list(img_arr.shape)
    shuffled_mark = shuffle_mark_image(mark_arr, img_arr, random_list_tuple)
    # 加 watermark
    # f_img_arr 是 img 的频域
    f_img_arr = np.fft.fft2(img_arr)
    fs_img_arr = np.fft.fftshift(f_img_arr)
    # f_out_img_arr 输出img的频域 ： f_img_arr + mark_encoded
    f_out_img_arr = fs_img_arr + alpha * shuffled_mark
    # fft 逆变换，输出空域的img arr
    fi_img_arr = np.fft.ifftshift(f_out_img_arr)
    out_img_arr = np.fft.ifft2(fi_img_arr)
    out_img_arr = np.abs(out_img_arr)

    # write to file
    cv2.imwrite('./imgs/encode_mark_img_3.jpg', out_img_arr)



