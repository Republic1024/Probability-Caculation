import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from random import*
import math

def change_image(image,n):
    width,height=image.size
    #转换成数组
    images=np.array(image)
    #判断是否可以整除
    if width%n!=0:
        w_change=int((width%n)/2)
        w1=w_change
        w2=width-w_change
    else:
        w1=0
        w2=width
    if height%n!=0:
        h_change=int((height%n)/2)
        h1=h_change
        h2=height-h_change
    else:
        h1=0
        h2=height
    image_crop=images[h1:h2,w1:w2,:]
    print(image_crop.shape)
    return image_crop,w2-w1,h2-h1

def cut_image(new_image,n):
    heights,widths=new_image.shape[0],new_image.shape[1]
    item_width=int(widths/n)
    item_height=int(heights/n)
    box_list=[]
    for i in range(0,n):
        for j in range(0,n):
            box=(j*item_width,i*item_height,(j+1)*item_width,(i+1)*item_height)#left,upper,right,lower
            box_list.append(box)
    image_list=[image.crop(box) for box in box_list]
    return image_list

def save_image(image_last):
    index=1
    for image in image_last:
        image.save(str(index)+'.jpg')
        index=index+1

def show_randomphoto2(image_list,n):
    shuffle(image_list)
    lists=[]
    c=[]
    for i in image_list:
        lists.append(np.array(i))
    #lists是数组
    for p in range(n):#n=3
        result=lists[p]#p=0
        for q in range(p+3,a,n):#1-9
            result=np.concatenate((result,lists[q]),axis=1)
        c.append(result)
    result2=c[0]
    for k in range(1,n):
        result2=np.concatenate((result2,c[k]),axis=0)
    plt.imshow(result2)
    plt.show()

def show_randomphoto(a,n):
    plt.figure()
    number=[]
    site=1
    for k in range(1,a+1):
        number.append(k)
    shuffle(number)
    for l in number:
        plt.subplot(n,n,site)
        images=Image.open(str(l)+'.jpg')
        images_a=np.array(images)
        plt.imshow(images)
        plt.xticks([])
        plt.yticks([])
        site=site+1
    plt.show()

image=Image.open('women.jpeg')
images=np.array(image)
print(images.shape)
a=int(input())
n=int(math.sqrt(a))
image_c,w,h=change_image(image,n)#改变图像像素
print(w,h)
image_list=cut_image(image_c,n)#切分
save_image(image_list)
#show_randomphoto(a,n)
show_randomphoto2(image_list,n)