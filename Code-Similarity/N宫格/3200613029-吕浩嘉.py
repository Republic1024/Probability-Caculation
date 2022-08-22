import numpy as np
import matplotlib.pyplot as plt
import random
from PIL import Image
image = Image.open("nit.jpg")
image = np.array(image)
ax, ay = 0, 0
n = 1
l = []
ax,ay = input().split(',')
ax,ay=eval(ax),eval(ay)
h=image.shape[0]
w=image.shape[1]
stepx=w//ax
stepy=h//ay

#切成x*y宫格
for i in range(ax):
    for j in range(ay):
        l.append(image[j*stepy:(j+1)*stepy, i*stepx:(i+1)*stepx, :])
xcnt,ycnt=0,0
#lx按列拼接成x块，ly按行拼接
lx=[]
ly=[]
random.shuffle(l)

while(ycnt<ay):
    while(xcnt<ax):
        lx.append(l.pop())
        xcnt+=1
    ly.append(np.concatenate(lx,axis=1))
    xcnt=0
    lx=[]
    ycnt+=1
res = np.concatenate(ly,axis=0)
plt.imshow(res)