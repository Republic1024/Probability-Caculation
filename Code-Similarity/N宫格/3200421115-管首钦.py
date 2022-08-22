import torch
import numpy as np
from PIL import Image
input_shape = 416
import cv2
import random
import matplotlib.pyplot as plt
image = Image.open(r'E:\PythonProject\yolo3-pytorch-master\yolo\Datasets\JPEGImages\2007_000027.jpg')
w, h = input_shape, input_shape

iw, ih = image.size

scale = min(w / iw, h / ih)
nw = int(iw * scale)
nh = int(ih * scale)
dx = (w - nw) // 2
dy = (h - nh) // 2
#---------------------------------#
#   将图像多余的部分加上灰条
#---------------------------------#
image = image.resize((nw, nh), Image.BICUBIC)
new_image = Image.new('RGB', (w, h), (128, 128, 128))
new_image.paste(image, (dx, dy))
new_image = cv2.cvtColor(np.asarray(new_image), cv2.COLOR_RGB2BGR)
cv2.imshow('daw', new_image)

def split_patch(img, n, image_size):
    ps = int(image_size / n)
    patchs = []
    for i in range(n):
        for j in range(n):
            patchs.append(img[i * ps:(i+1) * ps, j * ps:(j+1)*ps, :])
    return patchs



def show_image(n, patchs):
    ps = patchs.shape[2]
    mask = list(range(n * n))
    random.shuffle(mask)

    image = np.zeros((416, 416, 3), dtype=np.uint8)
    k = 0
    for i in range(n):
        for j in range(n):
            print(k)
            image[i * ps:(i+1) * ps, j * ps:(j+1)*ps, :] = patchs[mask[k]]
            k += 1
    return image

patchs = split_patch(new_image, 13, 416)
patchs = np.array(patchs)
image = show_image(13, patchs)
# print(image.shape)

cv2.imshow('img', image)
cv2.waitKey(0)
