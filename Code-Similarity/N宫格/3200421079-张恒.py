import random

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 读入图片
image = Image.open('nit.jpg')
image = np.array(image)
# 查看数据形状，其形状是[H, W, 3]，其中H代表高度， W是宽度，3代表RGB三个通道
print(image.shape)
# 显示原始图片
# plt.imshow(image)
n = eval(input())

# 居中裁切
cut=image.shape[0] % n
cut0=cut//2
cut1=cut-cut0
if cut1!=0:
    image = image[cut0:-cut1]
else:
    image = image[cut0:]


cut=image.shape[1] % n
cut0=cut//2
cut1=cut-cut0
if cut1!=0:
    image = image[:,cut0:-cut1]
else:
    image = image[:,cut0:]

print(image.shape)

x=image.shape[0]
y=image.shape[1]

# image=np.split(image,n,axis=0)
# np.random.shuffle(image)
# image = np.concatenate(image, axis=0)
#
# image=np.split(image,n,axis=1)
# np.random.shuffle(image)
# image = np.concatenate(image, axis=1)



def remake_image(image,n,lst):
    result=np.copy(image)
    h=image.shape[0]//n
    w=image.shape[1]//n
    for i in range(n**2):
        set=lst[i]
        h_num=set//n
        w_num=set%n
        rh_num=i//n
        rw_num=i%n
        # print(image[h_num*h:(h_num+1)*h,w_num*w:(w_num+1)*w,:])
        result[rh_num*h:(rh_num+1)*h,rw_num*w:(rw_num+1)*w,:]=image[h_num*h:(h_num+1)*h,w_num*w:(w_num+1)*w,:]
        # print(result[rh_num * h:(rh_num + 1) * h, rw_num * w:(rw_num + 1) * w, :])
    return result

list=[i for i in range(0,n**2)]
# print(list)
random.shuffle(list)
image=remake_image(image,n,list)


plt.imshow(image)
plt.show()
