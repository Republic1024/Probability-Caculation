import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math

image = Image.open(r"nit.jpg")
image = np.array(image)
print(image.shape)
x = int(math.sqrt(int(input("请输入需要切割成几宫格: "))))
H, W = image.shape[0], image.shape[1]
H1 = H
i = 0
while 1:
    if H1 % 3 == 0:
        break
    H1 = H1 - 1
    i = i + 1
if (H-H1)%2==1:
    H1 = (H-H1)//2+1
else:
    H1 = (H-H1)//2
H2 = H-i//2

W1 = W
i = 0
while 1:
    if W1 % 3 == 0:
        break
    W1 = W1 - 1
    i = i + 1
if (W-W1)%2==1:
    W1 = (W-W1)//2+1
else:
    W1 = (W-W1)//2
W2 = W-i//2
image_crop_h = image[H1:H2, W1:W2, :]
# plt.imshow(image_crop_h)
im_save = Image.fromarray(image_crop_h)
im_save.save('im_save.jpg')
image2 = Image.open('im_save.jpg')

new_image = np.array(image2)
arr = new_image.copy()
w1 = new_image.shape[1]
h1 = new_image.shape[0]
w2 = int(w1//x)
h2 = int(h1//x)
a = []
index = 1
for h in range(0, h1, h2):
    for w in range(0, w1, w2):
        tmp = image[h:h+h2, w:w+w2, :]
        a.append(tmp)
        index = index + 1

np.random.shuffle(a)

t = []
for i in range(0, len(a), x):
    t.append(np.concatenate(tuple(a[i:i+x]), axis=1))
arr = np.concatenate(tuple(t), axis=0)
plt.imshow(arr)
plt.show()