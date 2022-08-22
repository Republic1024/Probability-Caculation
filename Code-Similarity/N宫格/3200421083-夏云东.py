import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image = Image.open('picture.jpg')
image = np.array(image)


def crop_image(image, a, b):
    c = image.shape[0] % a
    c1 = c // 2
    c2 = c - c1
    if c1 != 0:
        image = image[c1:-c2]
    else:
        image = image[c1:-1]
    c = image.shape[1] % b
    c1 = c // 2
    c2 = c - c1
    if c1 != 0:
        image = image[:, c1:-c2]
    else:
        image = image[:, c1:-1]
    return image


def remake_image(image, a, b, lst):
    result = np.copy(image)
    high = image.shape[0] // a
    wide = image.shape[1] // b
    for i in range(a * b):
        set = lst[i] - 1
        h_num = set // b
        w_num = set % b
        rh_num = i // b
        rw_num = i % b
        result[rh_num * high:(rh_num + 1) * high, rw_num * wide:(rw_num + 1) * wide, :] = \
            image[h_num * high:(h_num + 1) * high, w_num * wide:(w_num + 1) * wide, :]
    return result


if __name__ == '__main__':
    image = Image.open('picture.jpg')
    image = np.array(image)
    print(image.shape)
    print("请输入切图的形式(a*b)：")
    a, b = input().split("*")
    a = int(a)
    b = int(b)
    cimage = crop_image(image, a, b)
    print(cimage.shape)
    rimage = remake_image(cimage, a, b, [9, 8, 7, 6, 5, 4, 3, 2, 1])
    plt.imshow(rimage)
    plt.show()
