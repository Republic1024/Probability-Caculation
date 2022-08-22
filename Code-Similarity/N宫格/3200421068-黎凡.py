
# coding: utf-8

# In[ ]:


import math
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random
#居中剪裁
def cen(w,h,n):
    lis=[]
    hx=0
    wx=0
    if w%n:
        temp=((w//n)*n)
        wx=int((w-temp)/2)
    if h%n:
        temp=((h//n)*n)
        hx=int((h-temp)/2)
    for i in range(wx,w-wx-1,w//n):
        for j in range(hx,h-hx-1,h//n):
            # print(i,j)
            lis.append(image[i:i+w//n,j:j+h//n,:])
    return lis
#九宫格
def nine(image):
    w,h,_=image.shape
    lis=[]
    if w%3:
        w=int(w//3*3)
    if h%3:
        h=int(h//3*3)
    for i in range(0,w,w//3):
        for j in range(0,h,h//3):
            lis.append(image[i:i+w//3,j:j+h//3,:])
    random.shuffle(lis)
    imag1=np.concatenate((lis[0],lis[1],lis[2]),axix=0)
    imag2=np.concatenate((lis[3],lis[4],lis[5]),axix=0)
    imag3=np.concatenate((lis[6],lis[7],lis[8]),axix=0)
    imag=np.concatenate((imag1,imag2,imag3),axix=1)
    plt.imshow(imag)
#随机分格
def grid(image,n):
    w, h, _ = image.shape
    print("{}宫格".format(n))
    n=int(math.sqrt(n))
    lis = cen(w, h, n)
    random.shuffle(lis)
    print("分出的块数：", len(lis))
    row = []
    for i in range(0, n**2, n):
        temp = []
        for j in range(i, i + n):
            temp.append(lis[j])
        tuple(temp)
        row.append(np.concatenate(temp, axis=0))
    tuple(row)
    imag = np.concatenate(row, axis=1)
    plt.imshow(imag)
    print(len(lis))
image = Image.open('rich.jpg')
plt.imshow(image)
image = np.array(image)
print(image.shape)
n=eval(input())
grid(image,n)
plt.show() 

