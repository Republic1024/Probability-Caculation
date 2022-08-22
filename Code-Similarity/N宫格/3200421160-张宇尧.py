import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math
import random

# 读入图片
im = Image.open('nit.jpg')
im = np.array(im)

# 输入一个数字并计算行数和列数
n = int(input())
row = int(math.sqrt(n))
print(row)

# 高度和宽度
H, W = im.shape[0], im.shape[1]
height = H // row
width = W // row
rmod = H % row
cmod = W % row

# 高度和宽度的起始像素和结束像素
strow = rmod // 2
stcol = cmod // 2
edrow = strow + row * height
edcol = stcol + row * width

List = []
for h in range(strow, edrow, height):
    for w in range(stcol, edcol, width):
        temp = im[h:h + height, w:w + width, :]
        List.append(temp)

random.shuffle(List)
List1 = []
for i in range(row):
    img = List[i * row]
    for j in range(row - 1):
        img = np.concatenate((img, List[j + i * row + 1]), axis=1)
    List1.append(img)
img1 = List1[0]

for i in range(1, row):
    img1 = np.concatenate((img1, List1[i]), axis=0)

plt.imshow(img1)
plt.show()
