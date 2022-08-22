import math
import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image = Image.open('IMG_1552.JPG')
print("请输入要获得的宫格数:")
n=eval(input())

x=int(math.sqrt(n))#x和b是根据输入的n确定的要分成x*b型
b=int(n/x)

image = np.array(image)
plt.imshow(image)
plt.show()

H,W=image.shape[0],image.shape[1]#H，W是整张照片的长和宽
height=int(H//x)#height是每一格的长
width=int(W//b)#width是每一格的宽
re_h=H%height#取余
re_w=W%width
re_hr=int(re_h//2)#整除2得到后续剧中裁剪应该删去的长度
re_wr=int(re_w//2)
a=[]
for h in range(re_hr,H-re_hr-1,height):#居中裁剪
    for w in range(re_wr,W-re_wr-1,width):
        temp=image[h:h+height,w:w+width,:]
        a.append(temp)#把每一格都存入列表a中

list1=random.sample(list(range(n)), n)#随机生成一个列表，代表拼接的图片块是随机的
list2=random.sample(list(range(int(x))), int(x))
co=[]
for i in range(0,len(list1),int(b)):
    temp=a[list1[i]]
    for j in range(1,int(b)):
        temp=np.concatenate((temp,a[list1[i+j]]),axis=0)#把temp和任意一块拼起来，b块为一行
    co.append(temp)
rw=co[list2[0]]
for i in range(1,int(x)):#把每一行拼接起来
    rw=np.concatenate((rw,co[list2[i]]),axis=1)#axis=1代表把一行一行的拼成一列
plt.imshow(rw)
plt.show()
