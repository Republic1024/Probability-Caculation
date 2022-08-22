import math
import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image = Image.open('eg.jpg')
print("输入宫格数:")
n=eval(input())
x=int(math.sqrt(n))
image = np.array(image)

H,W=image.shape[0],image.shape[1]
height=int(H//x)
width=int(W//x)
h_y=H%height
w_y=W%width

a=[]
for h in range(int(h_y//2),H-h_y,height):
    for w in range(int(w_y//2),W-w_y,width):
        tmp=image[h:h+height,w:w+width,:]
        a.append(tmp)
xl=random.sample(list(range(n)), n)

lie=[]
for i in range(0,len(xl),int(x)):
    tmp=a[xl[i]]
    for j in range(1,int(x)):
        tmp=np.concatenate((tmp,a[xl[i+j]]),axis=0)
    lie.append(tmp)
tu=[]
tu=np.concatenate((lie),axis=1)

plt.imshow(tu)
plt.show()