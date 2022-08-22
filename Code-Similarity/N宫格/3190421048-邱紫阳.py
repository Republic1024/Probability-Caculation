import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
# 引入模块

# 读入图片
n=int(input("请输入一个整数:"))
image = Image.open('nit.jpg')
imagedata = np.array(image)
# 查看数据形状，其形状是[H, W, 3]，其中H代表高度， W是宽度，3代表RGB三个通道
print(imagedata.shape)
# 显示原始图片
plt.imshow(imagedata)
plt.show()

H, W = imagedata.shape[0], imagedata.shape[1]
# 注意此处用整除，H是高，W是宽必须为整数
print(H)
print(W)

H1 = H // 2
H2 = H

W1 = 0
W2 = W//5

cnt=0
figure_save_path = "pictures"

for i in range(0,n):
    for j in range(0,n):
        H1=H//n*i
        H2=H//n*(i+1)
        W1=H//n*j
        W2=H//n*(j+1)
        image_crop_w = imagedata[H1:H2, W1:W2, :]
        # plt.imshow(image_crop_w)
        im_save = Image.fromarray(image_crop_w)
        # im_save.save('im_save.jpg')
        im_save.save('pictures/{:.0f}.jpg'.format(cnt))
        # plt.savefig(os.path.join(figure_save_path, '{:.0f}.jpg'.format(cnt)))
        cnt+=1


paths = []
n=int(input())
for i in range (0,n*n):
    paths.append(f'pictures/{i}.jpg')
    # print(paths)
    # print("sdfsdfjdshkjfkj")


cnt=100

img_array = ''
img = ''
for i, v in enumerate(paths):
    # i为每个图像的序号, x为每个图像的多维像素矩阵
    if i % n==0:
        img = Image.open(v)  # 打开图片
        img_array = np.array(img)  # 转化为np array对象
        # print(img_array)
    else:
        img_array2 = np.array(Image.open(v))
        img_array = np.concatenate((img_array, img_array2), axis=1)  # 横向拼接
        # img_array = np.concatenate((img_array, img_array2), axis=0)  # 纵向拼接

    if (i+1)%n==0:
        img = Image.fromarray(img_array)
        # 实现矩阵到图片的转化
        # img.save('test.jpg')
        img.save('pictures/{:.0f}.jpg'.format(cnt))
        cnt+=1


paths = []
n=int(input())
for i in range (0,n):
    paths.append(f'pictures/{i+100}.jpg')
    # print(paths)
    # print("sdfsdfjdshkjfkj")


cnt=1000

img_array = ''
img = ''
for i, v in enumerate(paths):
    # i为每个图像的序号, x为每个图像的多维像素矩阵
    if i ==0:
        img = Image.open(v)  # 打开图片
        img_array = np.array(img)  # 转化为np array对象
        # print(img_array)
    else:
        img_array2 = np.array(Image.open(v))
        # img_array = np.concatenate((img_array, img_array2), axis=1)  # 横向拼接
        img_array = np.concatenate((img_array, img_array2), axis=0)  # 纵向拼接

    if (i+1)%n==0:
        img = Image.fromarray(img_array)
        # 实现矩阵到图片的转化
        # img.save('test.jpg')
        img.save('pictures/{:.0f}.jpg'.format(cnt))