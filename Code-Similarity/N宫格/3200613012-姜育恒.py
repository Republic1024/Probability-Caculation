import numpy as np
import matplotlib.pyplot as plt
import random
from PIL import Image
image = Image.open("nit.jpg")
image = np.array(image)
x, y = 0, 0
n = 1
l = []
x,y = input().split(',')
x,y=eval(x),eval(y)
h=image.shape[0]
w=image.shape[1]
stepx=w//x
stepy=h//y
# 切成x*y宫格
for i in range(x):
    for j in range(y):
        l.append(image[j*stepy:(j+1)*stepy, i*stepx:(i+1)*stepx, :])
xcnt,ycnt=0,0
# lx按列拼接成x块，ly按行拼接
lx=[]
ly=[]
# 打乱列表内部顺序，以便后面pop输出乱序
random.shuffle(l)
while(ycnt<y):
    while(xcnt<x):
        lx.append(l.pop())
        xcnt+=1
    ly.append(np.concatenate(lx,axis=1))
    xcnt=0
    lx=[]
    ycnt+=1
res = np.concatenate(ly,axis=0)
plt.imshow(res)
