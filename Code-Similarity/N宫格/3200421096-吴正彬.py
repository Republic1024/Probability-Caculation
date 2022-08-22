import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from pylab import *

n = eval(input("输入："))


image = Image.open('nit.jpg')
image = np.array(image)


H, W = image.shape[0], image.shape[1]
mod_h = H % n
mod_w = W % n
if mod_h % 2 == 1:
    image = np.delete(image, np.s_[H - (mod_h // 2 + 1): H], 0)
else:
    image = np.delete(image, np.s_[H - (mod_h // 2): H], 0)
image = np.delete(image, np.s_[0: mod_h // 2], 0)
if mod_w % 2 == 1:
    image = np.delete(image, np.s_[W - (mod_w // 2 + 1): W], 1)
else:
    image = np.delete(image, np.s_[W - (mod_w // 2): W], 1)
image = np.delete(image, np.s_[0: mod_w // 2], 1)
W -= mod_w
H -= mod_h
w = W // n
h = H // n


a = [i for i in range(n * n)]
np.random.shuffle(a)


image1 = []
for i in range(0, H, h):
    for j in range(0, W, w):
        image_crop = image[i: i + h, j: j + w, :]
        image1.append(image_crop)


image_h = []
for i in range(n):
    image_htmp = image1[a[i * n]]
    for j in range(1, n):
        image_htmp = np.hstack((image_htmp, image1[a[i * n + j]]))
    image_h.append(image_htmp)


image_end = image_h[0]
for i in range(1, n):
    image_end = np.vstack((image_end, image_h[i]))
plt.imshow(image_end)
show()