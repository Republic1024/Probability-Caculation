from PIL import Image
import matplotlib.pyplot as plt
import glob
import numpy as np
from cv2 import imread, imwrite
import random


number=eval(input("输入规格："))
#打开图像
image = Image.open("cdc9f3cc7c43233.jpg")
image = np.array(image)
print(image.shape)

cols=image.shape[0]
rows=image.shape[1]

#根据输入的数进行裁剪
#记录列、行的余量：

cols_last = (cols % number)/2
rows_last = (rows % number)/2

#先进行整体的裁剪

cols_lower = int(cols_last)
cols_upper = int(cols-cols_last)
rows_lower = int(rows_last)
rows_upper = int(rows-rows_last)
print(cols_lower,cols_upper)
print(rows_last,rows_upper)
roi = image[cols_lower:cols_upper,rows_lower:rows_upper,:]
plt.imshow(roi)
plt.show()
plt.imsave('test.jpg',roi)

cols_number=cols-cols%number
cols_number=cols_number/number
rows_number=rows-cols%number
rows_number=rows_number/number


col_start=cols_lower
rows_start=rows_lower
count=0
for i in range(number):
    cols_lower = int(col_start + cols_number * i)
    for j in range(number):
        rows_lower=int(rows_start+rows_number*j)
        roi = image[cols_lower:int(cols_lower+cols_number), rows_lower:int(rows_lower+rows_number), :]
        plt.imshow(roi)
        # plt.show()
        plt.imsave('picture/test{}.jpg'.format(count), roi)
        count += 1



imgs, heights, widths = [], [], []
for f in glob.glob("picture/*.jpg"):
    img = imread(f, -1)  # 参数-1表示返回原图
    imgs.append(img)


lst = [i for i in range(number*number)]
random.shuffle(lst)

cnt1 = 0
cnt2 = 0
ls = []
i = 0
while i < number*number:
    ls2 = []
    for j in range(number):
        print(i)
        ls2.append(imgs[lst[i]])
        i += 1
    ls.append(ls2)

ls3 = []
for i in range(number):
    img = np.concatenate(ls[i], 1)
    ls3.append(img)
img9 = np.concatenate(ls3, 0)
imwrite("result.jpg", img9)