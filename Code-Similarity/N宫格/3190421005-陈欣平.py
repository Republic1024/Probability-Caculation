import numpy as np
import math
import matplotlib.pyplot as plt
import cv2 as cv
import random
def reShape(img,n):
    size = img.shape
    h = size[0]
    w = size[1]

    if h%n!=0:
        h=int(h-h%n)
    if w%n!=0:
        w=int(w-w%n)
    newimg = cv.resize(img, (w,h))
    return newimg

def cut_img(img,n):
    h, w = img.shape[0:2]
    h = int(h / n)
    w = int(w / n)

    crop_list = []
    for i in range(0, n):
        for j in range(0, n):
            box = (i * h, j * w, (i + 1) * h, (j + 1) * w)
            crop_list.append(img[box[0]:box[2], box[1]:box[3]])
    return crop_list

def show(imgs,n):
    img=[]
    random.shuffle(imgs)
    for i in range(0,n):
        img.append(cv.hconcat(imgs[(i*n):(i*n+n)]))
    image=cv.vconcat(img)
    cv.imshow("window4", image)
    cv.waitKey(0)

img=cv.imread("Joimage.jpg",-1)
x,y=img.shape[0:2]
x=int(x/2)
y=int(y/2)
img=cv.resize(img,(y,x))

print("-----------------------")
print("--------0.正放---------")
print("-------1.镜像倒放-------")
print("--------2.倒放---------")
print("---------3.n宫格-------")
print("---------4.退出--------")
while 1:
    choice=input("请输入选项：")
    if choice == "0":
        cv.imshow("window0", img)
        cv.waitKey(0)
    elif choice == "1":
        cv.imshow("window1", img[::-1])
        cv.waitKey(0)
    elif choice == "2":
        cv.imshow("window2", img[::-1, ::-1, :])
        cv.waitKey(0)
    elif choice == "3":
        n=int(input("输入几宫格： "))
        n = int(math.sqrt(n))
        img = reShape(img, n)
        imgs =  cut_img(img,n)
        show(imgs,n)
    elif n == "4":
        break;
cv.destroyAllWindows()