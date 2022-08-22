import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math

def cut_image(image,n):
    #width 是宽，height 是长
    width,height= image.size
    print(height, width)
    #不能被整除就向中心裁剪
    x = 0
    y = 0
    if width % n != 0:
        x = width % n
        if x % 2 != 0:
            x = x + n
    if height % n != 0:
        y = height % n
        if y % 2 != 0:
            y = y + n
    image = image.crop((x//2 , y //2 ,width - x//2 ,height - y//2))
    new_width = int(width // n)
    new_height = int(height // n)
    box_list=[]
    for i in range(0,n):
        for j in range(0,n):
            box = (j * new_width, i * new_height, (j+1) * new_width, (i + 1) * new_height)
            box_list.append(box)
    image_list = [image.crop(box) for box in box_list]
    return image_list


def merge_picture(image_list,n):
    arr = []
    for i in image_list:
        arr.append(np.array(i))
    #print(arr)
    random.shuffle(arr)
    temp = []
    print(len(arr))
    for i in range(0,len(arr),n):
        temp.append(np.concatenate(tuple(arr[i:i+n]),axis=1))
    plt.imshow(np.concatenate(tuple(temp),axis=0))
    plt.show()


if __name__ == '__main__':
    image = Image.open("picture.jpg")
    n = eval(input())
    n = int(math.sqrt(n))
    image_list = cut_image(image,n)
    merge_picture(image_list, n)