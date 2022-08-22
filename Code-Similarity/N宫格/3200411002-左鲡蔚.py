import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math

image = Image.open(r"C:\\Users\\18431\\Desktop\\nit.jpg")
image = np.array(image)
print(image.shape)
x = input("请输入要裁剪成几宫格：")
x = int(x)
x = int(math.sqrt(x))
height,width = image.shape[0], image.shape[1]
h,w = image.shape[0], image.shape[1]
if width % x !=0:
    w = x- w % x + w
if height % x !=0:
    h = x - h % x + h
#建立全黑图像
image= Image.fromarray(image)
new_image = Image.new('RGB',(w,h),(0,0,0))
new_image.paste(image,box=((w-width)//2,(h-height)//2,(w-width)//2+image.width,(h-height)//2+image.height),mask=None)


new_image = np.array(new_image)
arr = new_image.copy()
w1 = new_image.shape[1]
h1 = new_image.shape[0]
w = int(w//x)
h = int(h//x)
arr = np.split(arr, range(h, h1, h), axis=0)#切割 axis = 0 横切
np.random.shuffle(arr)#随机图片
arr = np.concatenate(arr, axis=0)#拼在一起
arr = np.split(arr, range(w, w1, w), axis=1)#切割 axis = 1 纵切
np.random.shuffle(arr)
arr = np.concatenate(arr, axis=1)
print(type(arr))
plt.imshow(arr)
plt.show()