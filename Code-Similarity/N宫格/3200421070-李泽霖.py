import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 读入图片
image = Image.open('nit.jpg')
image = np.array(image)

def crop_image(image,a,b): # 默认切为九宫格
    H=image.shape[0]//a*a
    W=image.shape[1]//b*b
    return image[:H,:W,:]

def remake_image(image,a,b,lst): # 设lst=[7,1,3,6,4,2,5,9,8]
    result=np.copy(image)
    h=image.shape[0]//a
    w=image.shape[1]//b
    for i in range(a*b):
        set=lst[i]-1
        h_num=set//b  # 从1开始
        w_num=set%b  # 从1开始
        rh_num=i//b
        rw_num=i%b
        result[rh_num*h:(rh_num+1)*h,rw_num*w:(rw_num+1)*w,:]=image[h_num*h:(h_num+1)*h,w_num*w:(w_num+1)*w,:]
    return result


if __name__ == '__main__':
    # 读入图片
    image = Image.open('nit.jpg')
    image = np.array(image)

    print(image.shape)

    print("请输入切图的形式(例如：3*3)：")
    a,b=input().split("*") # a为行切，b为列切
    a=int(a)
    b=int(b)

    cimage=crop_image(image,a,b)
    print(cimage.shape)

    rimage=remake_image(cimage,a,b,[7,1,3,6,4,2,5,9,8,10])

    # 显示原始图片
    plt.imshow(rimage)
    plt.show()