import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
a=[]
im = Image.open('nit.jpg')
im=np.array(im)
H,W=im.shape[0]-2,im.shape[1]-1
height=int(H/3)
width=int(W/3)
for h in range(1,H+1,height):#这样可以做到左右各去掉一个像素
    for w in range(0,W,width):
        tmp=im[h:h+height,w:w+width,:]
        a.append(tmp)
list=[0,1,2,3,4,5,6,7,8]
b = random.sample(list, 9)
c=[]
for i in range(0,len(b),3):
    c.append(np.concatenate((a[b[i]],a[b[i+1]],a[b[i+2]]),axis=1))
plt.imshow(np.concatenate((c[0],c[1],c[2]),axis=0))