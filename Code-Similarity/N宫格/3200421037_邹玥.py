import math
import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image = Image.open('nit.jpg')
image = np.array(image)
plt.imshow(image)

print("拆分个数:")
n = eval(input())
x = int(math.sqrt(n))
b = int(n / x)
H, W = image.shape[0], image.shape[1]
height = int(H // x)
width = int(W // b)
rem_h = H % height
rem_w = W % width
rem_hr = int(rem_h // 2)
rem_wr = int(rem_w // 2)
a = []
for i in range(rem_hr, H - rem_hr - 1, height):
    for j in range(rem_wr, W - rem_wr - 1, width):
        tmp = image[i:i + height, j:j + width, :]
        a.append(tmp)
m = random.sample(list(range(n)), n)
t = random.sample(list(range(int(x))), int(x))
co = []
for i in range(0, len(m), int(n)):
    tmp = a[m[i]]
    for j in range(1, int(n)):
        tmp = np.concatenate((tmp, a[m[i + j]]), axis=0)
    co.append(tmp)
rw = co[t[0]]
for i in range(1, int(x)):
    rw = np.concatenate((rw, co[t[i]]), axis=1)
plt.imshow(rw)
plt.show()
