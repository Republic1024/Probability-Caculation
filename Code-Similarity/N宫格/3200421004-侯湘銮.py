#-*- coding = utf-8 -*-
#@Time : 2022/5/2 10:00
#@Author : hou
#@File : p.py
#@Software : PyCharm

from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as img
import cv2
import numpy as np
from math import sqrt

"""#cv2创建图像
im = cv2.imread("nit.jpg")
cv2.namedWindow('region',cv2.WINDOW_NORMAL)
cv2.imshow("region",im)
cv2.waitKey()
cv2.destroyAllWindows()"""



#读入图片
# im = Image.open("nit.jpg")
im = img.imread("nit.jpg")

im = np.array(im) #转化成数组
#print(im.shape)  (200, 301, 3)
#查看数据形状，其形状是[H, W, 3]

#使其可以被3整除
im = np.delete(im,[0,199],axis=0)
im = np.delete(im,300,axis=1)
# print(im.shape) #(198, 300, 3)

#分割成九宫格
n = 9  #图像切割数量
H, W = im.shape[0], im.shape[1]
height = H//3
width = W//3
print(height,width)  #66 100
im_res = {}
im_width = np.split(im,range(0,W+1,width),axis = 1)
for i in range(1,n+1):
    im_res[i] = np.split(im_width[i],range(0,H+1,width),axis = 0)

pic_list = []
for i in range(0,3):
    for j in range(0,3):
        # c = im[width * i:width * (i + 1), height * j:height * (j + 1)]
        pic = (j * width, i * width, (j + 1) * width, (i + 1) * width)
        pic_list.append(pic)

image_list = [im.crop(pic) for pic in pic_list]

#保存图片
index = 1
for image in pic_list:
    image.save('./result/python' + str(index) + '.png', 'PNG')
    index += 1


