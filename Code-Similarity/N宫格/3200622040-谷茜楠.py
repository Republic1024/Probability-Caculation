import math
import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image = Image.open('photo.jpg')
print("请输入要获得的宫格数:")
n = int(input())
x = int(math.sqrt(n))
b = int(n/x)
image = np.array(image)
plt.imshow(image)
plt.show()
H, W = image.shape[0], image.shape[1]     #长、宽
height = int(H//x)             #every
width = int(W//b)
h0 = H % height
w0 = W % width
h1 = int(h0//2)          #两边各需要裁剪的距离
w1 = int(w0//2)
l = []
for h in range(h1, H-h0, height):          #居中裁剪
    for w in range(w1, W-w0, width):
        tmp = image[h:h+height, w:w+width, :]
        l.append(tmp)
m = random.sample(list(range(n)), n)        #图片块随机生成
p = random.sample(list(range(int(x))), int(x))
coun = []
for i in range(0, len(m), b):
    tmp = l[m[i]]
    for j in range(1, b):
        tmp = np.concatenate((tmp, l[m[i+j]]), axis=0)
    coun.append(tmp)
rw = coun[p[0]]
for i in range(1, int(x)):
    rw = np.concatenate((rw, coun[p[i]]), axis=1)
plt.imshow(rw)
plt.show()


