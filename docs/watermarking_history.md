```python
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt



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
img = Image.open('./imgs/gl1.jpg')
mark = Image.open('./imgs/watermark.jpg')
fig = plt.figure('原图')
img_fig = fig.add_subplot(1, 1, 1)
plt.imshow(img)
plt.show()
```