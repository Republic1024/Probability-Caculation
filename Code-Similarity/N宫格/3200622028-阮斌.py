import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math
import random

# 读入图片
im = Image.open('ruanbin.jpg')
im = np.array(im)
# plt.imshow(im)
# 输入一个数字并计算行数和列数
n = int(input())
row = int(math.sqrt(n))
# print(row)

# 高度和宽度
H, W = im.shape[0], im.shape[1]
height = H // row
width = W // row
# 宽度和高度取模
rowmod = H % row
colmod = W % row
# 高度和宽度的起始像素和结束像素
startrow = rowmod // 2
startcol = colmod // 2
endrow = startrow + row * height
endcol = startcol + row * width

List = []
for h in range(startrow, endrow, height):
    for w in range(startcol, endcol, width):
        temp = im[h:h + height, w:w + width, :]
        List.append(temp)
        # plt.imshow(temp)
# print(len(List))
random.shuffle(List)
List1 = []
for i in range(row):
    img = List[i * row]
    for j in range(row - 1):
        img = np.concatenate((img, List[j + i * row + 1]), axis=1)
    List1.append(img)
# print(len(List1))
# print(List1)
img1 = List1[0]
# print(img1)
for i in range(1, row):
    img1 = np.concatenate((img1, List1[i]), axis=0)
plt.imshow(img1)
plt.show()