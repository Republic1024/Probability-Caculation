from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
def preprocess(image,n):
    width,height=image.size
    cut_width=width%n
    cut_height=height%n
    left=cut_width//2
    right=cut_width-left
    down=cut_height//2
    up=cut_height-down

    midimage=(left,down,width-right,height-up)
    return image.crop(midimage)
def cutprocess(image,n):
    width, height = image.size
    print(image.size)
    cutwidth=width//n
    cutheight=height//n
    list=[]
    for i in range(0,n):
        for j in range(0,n):
            listtem=(j*cutwidth,i*cutheight,(j+1)*cutwidth,(i+1)*cutheight)
            list.append(listtem)
    image_list=[image.crop(tem) for tem in list]
    print(image_list)
    return image_list
def imageshow(image_list,n):

    image=image_list[0]
    print(image_list)
    cwidth,cheight=image.size
    print(image.size)
    imagetarget=(cwidth*n,cheight*n)
    background=Image.new('RGBA',imagetarget,(0,0,0,0))

    for ind,img in enumerate(image_list):
        if img.mode != "RGBA":
            img = img.convert("RGBA")
        # print(ind)
        row,col=ind//n,ind%n
        location=(col*cwidth,row*cheight)
        background.paste(img,location)

    background.show()



image=Image.open("home.jpg")
print("Please input the block you want:")
n=int(input())
image=preprocess(image,n)
image_list=cutprocess(image,n)
np.random.shuffle(image_list)
show=imageshow(image_list,n)

