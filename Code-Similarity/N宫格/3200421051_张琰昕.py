import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

weight = int(input("横向分为几格"))
height = int(input("纵向分为几格"))

img = np.array(Image.open("photo.jpg"))
imgsr = img.shape
new_img = Image.new('RGB', (imgsr[1], imgsr[0]))

heightm = imgsr[0]//height
weightm = imgsr[1]//weight
hgp = (imgsr[0] % heightm)//2
vgp = (imgsr[1] % weightm)//2

h = range(hgp, imgsr[0]+1-hgp, heightm)
v = range(vgp, imgsr[1]+1-vgp, weightm)

show_list = []

for i in range(1, height+1):
    for j in range(1, weight+1):
        show_list.append(img[h[i-1]:h[i], v[j-1]:v[j]])

np_arr = np.array(show_list)
final_order = np.array(range(0, height*weight))
np.random.shuffle(final_order)
idx = 0

for i in range(1, height+1):
    for j in range(1, weight+1):
        imgm = Image.fromarray(np_arr[final_order[idx]])
        new_img.paste(imgm, box=(v[j-1], h[i-1], v[j], h[i]))
        idx += 1

plt.imgshow(new_img)
plt.show()
