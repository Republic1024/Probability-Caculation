import matplotlib.pyplot as plt
import random
import numpy as np
from PIL import Image
image=Image.open("听写.jpg")
image=np.array(image)
x, y=0, 0
n=1
l=[]
x,y=input().split(',')
x,y=eval(x),eval(y)
h=image.shape[0]
w=image.shape[1]
stepx=w//x
stepy=h//y
for i in range(x):
    for j in range(y):
        l.append(image[j*stepy:(j+1)*stepy, i*stepx:(i+1)*stepx, :])
xcnt,ycnt=0,0
lx=[]
ly=[]
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
