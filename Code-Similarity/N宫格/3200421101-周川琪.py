import os
import random

from PIL import Image
import glob
import numpy as np
import math
from cv2 import imread,imwrite#图像读取，图像写入
# 读取图片
im = Image.open('R-C.jpg')

N=int(input())
n=int(math.sqrt(N))

# 宽高各除n，获取裁剪后的单张图片大小
width = im.size[0]//n
height = im.size[1]//n

# 裁剪图片的左上角坐标
start_x = 0
start_y = 0

# 用于给图片命名
im_name = 1

# 循环裁剪图片
for i in range(n):
    for j in range(n):
        # 裁剪图片并保存
        crop = im.crop((start_x, start_y, start_x+width, start_y+height))
        # 判断文件夹是否存在
        if not os.path.exists('zhm'):
            os.mkdir('zhm')
        crop.save('zhm/' + str(im_name) + '.jpg')

        # 将左上角坐标的 x 轴向右移动
        start_x += width
        im_name += 1

    # 当第一行裁剪完后 x 继续从 0 开始裁剪
    start_x = 0
    # 裁剪第二行
    start_y += height


im,hei,wid=[],[],[]
for f in glob.glob("zhm/*.jpg"):
    img=imread(f,-1)
    print("ori:",img.shape)
    h,w=img.shape[:2]
    hei.append(h)
    wid.append(w)
    im.append(img)

minhei=min(hei)
minwid=min(wid)
for i,x in enumerate(im):
    im[i]=x[:minhei:n,:minwid:n,:]
    print("thum:",im[i].shape)


imgx=[]
for i in range(n):
    imgx.append(0)
    a=im[i*n:(i+1)*n]
    np.random.shuffle(a)
    imgx[i]=np.concatenate(a,1)
    print(imgx[i].shape)
    print("-------------------------")
b=[imgx[i] for i in range(n)]
np.random.shuffle(b)
img_n = np.concatenate(b, 0)
print("n*n_shape:",img_n.shape)
imwrite("concat_zhm.jpg",img_n)


im = Image.open("concat_zhm.jpg").resize((320,288))
im.save("zhm_2.jpg")

