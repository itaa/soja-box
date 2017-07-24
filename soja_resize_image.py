import cv2


def resize_image(img_path, mini_size=480, jpeg_quality=80):
    """
    缩放image
    :param img_path: image的路径
    :param mini_size: 最小边的尺寸
    :param jpeg_quality: jpeg图片的质量
    """
    org_img = cv2.imread(img_path)
    img_w = org_img.shape[0]
    img_h = org_img.shape[1]
    if max(img_w, img_h) > mini_size:
        if img_w > img_h:
            img_w = mini_size * img_w // img_h
            img_h = mini_size
        else:
            img_h = mini_size * img_h // img_w
            img_w = mini_size
    dist_size = (img_h, img_w)
    r_image = cv2.resize(org_img, dist_size, interpolation=cv2.INTER_AREA)
    params = [cv2.IMWRITE_JPEG_QUALITY, jpeg_quality]
    img_name = img_path + '_New.jpg'
    cv2.imwrite(img_name, r_image, params=[cv2.IMWRITE_JPEG_QUALITY, params])


if __name__ == '__main__':
    resize_image('./imgs/encode_mark_img.jpg')

