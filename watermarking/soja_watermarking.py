#!/usr/bin/env python3
# Create by ChunYing.Jia

import numpy as np
import matplotlib.pyplot as plt
import cv2


def resize_image(image, dist_size):
    """
    缩放图像
    :param image:
    :param dist_size:
    :return:
    """
    # 缩放前按照最小边裁剪裁剪
    h, w, m = image.shape
    mini = min(h, w)
    margin_h = (h - mini) / 2
    margin_w = (w - mini) / 2
    c_image = np.zeros((mini, mini, m))
    c_image[:, :, :] = image[margin_h:h-margin_h, margin_w:w-margin_w, :]
    # 如果想要收缩图像，那么使用重采样差值法效果最好；
    # 如果想要放大图像，那么最好使用3次差值法或者线性差值法（文档推荐的）
    # 这里是缩放所以采用 INTER_AREA
    # interpolation 简介：
    # interpolation - 插值方法。共有5种：
    # １）INTER_NEAREST - 最近邻插值法
    # ２）INTER_LINEAR - 双线性插值法（默认）
    # ３）INTER_AREA - 基于局部像素的重采样（resampling using pixel area relation）。
    # 对于图像抽取（image decimation）来说，这可能是一个更好的方法。
    # 但如果是放大图像时，它和最近邻法的效果类似。
    # ４）INTER_CUBIC - 基于4x4像素邻域的3次插值法
    # ５）INTER_LANCZOS4 - 基于8x8像素邻域的Lanczos插值
    r_image = cv2.resize(c_image, dist_size, interpolation=cv2.INTER_AREA)
    return r_image


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
    :return:shuffle_mark
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


def add_watermarking(i_image_name, m_image_name, o_image_name, output_size, alpha=1.0, shuffle_list=None):
    """
    给图片添加水印
    :param i_image_name: original 输入 image name
    :param m_image_name: mark image
    :param o_image_name: marked 输出 image name
    :param output_size: 输出图片的大小
    :param alpha: 水印的清晰度, 默认高清
    :param shuffle_list: 用来打散mark的随机数列，默认为空，会随机生成，并返回
    :return: marked image
    """
    img_arr = cv2.imread(i_image_name)
    img_arr = resize_image(img_arr, output_size)
    mark_arr = cv2.imread(m_image_name)
    if shuffle_list is None:
        shuffle_list = generate_random_list(img_arr.shape)
    shuffled_mark = shuffle_mark_image(mark_arr, img_arr, shuffle_list)
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
    cv2.imwrite(o_image_name, out_img_arr)

if __name__ == "__main__":
    original_image_name = './imgs/gl1.jpg'
    output_image_name = './imgs/encode_mark_img_4.jpg'
    watermark_image = './imgs/pnrmark.png'
    alpha = 1.0
    output_size = (176, 176)
    add_watermarking(original_image_name, watermark_image, output_image_name, output_size=output_size)

