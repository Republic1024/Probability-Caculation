import math
import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
image = Image.open('173.jpg')
print("请输入要获得的宫格数:")
n=eval(input())
x=int(math.sqrt(n))
b=int(n/x)
image = np.array(image)
#print(image.shape)
plt.imshow(image)
plt.show()
H,W=image.shape[0],image.shape[1]
height=int(H//x)
width=int(W//b)
rem_h=H%height
rem_w=W%width
rem_hr=int(rem_h//2)
rem_wr=int(rem_w//2)
a=[]
for h in range(rem_hr,H-(rem_h-rem_hr),height):
    for w in range(rem_wr,W-(rem_w-rem_wr),width):
        tmp=image[h:h+height,w:w+width,:]
        a.append(tmp)
l=random.sample(list(range(n)), n)
r=random.sample(list(range(int(x))), int(x))
co=[]
for i in range(0,len(l),int(b)):
    tmp=a[l[i]]
    for j in range(1,int(b)):
        tmp=np.concatenate((tmp,a[l[i+j]]),axis=0)
    co.append(tmp)
rw=co[r[0]]
for i in range(1,int(x)):
    rw=np.concatenate((rw,co[r[i]]),axis=1)
plt.imshow(rw)
plt.show()