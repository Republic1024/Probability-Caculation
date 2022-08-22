import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

vv = int(input("宽分为几格"))
hh = int(input("高分为几格"))


im = Image.open("1.jpg")
im = np.array(im)


srr = im.shape
imnew = Image.new('RGB',(srr[1],srr[0]))

hm = srr[0]//hh
vm = srr[1]//vv

hgp = (srr[0]%hm)//2
vgp = (srr[1]%vm)//2

h = range(hgp,srr[0]+1-hgp,hm)
v = range(vgp,srr[1]+1-vgp,vm)


l = []


for i in range(1,hh+1):
    for j in range(1,vv+1):
        hg = h[i-1]
        vg = v[j-1]
        hn = h[i]
        vn = v[j]
        l.append(im[hg:hn,vg:vn])

np_arr = np.array(l)
orde = np.array(range(0,hh*vv))
np.random.shuffle(orde)


idx = 0

for i in range(1,hh+1):
    for j in range(1,vv+1):
        hg = h[i-1]
        vg = v[j-1]
        hn = h[i]
        vn = v[j]
        
        imm = Image.fromarray(np_arr[orde[idx]])
        imnew.paste(imm,box = (vg,hg,vn,hn))
        
        idx += 1

plt.imshow(imnew)
plt.show()