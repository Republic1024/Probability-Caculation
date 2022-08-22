import random
from PIL import Image
import matplotlib.pyplot as plt

n = int(input())
image = Image.open('nit.jpg')
w, h = image.size

item_w = w//n
item_h = h//n
image.resize([(item_h*n),(item_w*n)])
collections_list = []

for i in range(0,n):
    for j in range(0,n):
        collections = (j*item_w,i*item_h,(j+1)*item_w,(i+1)*item_h)
        collections_list.append(collections)
image_list = []
for box in collections_list:
    image_list.append(image.crop(box))
random.shuffle(image_list)


def image_concat(image_list, number):
    image = image_list[0]
    width, height = image.size
    target_shape = (number * width, number * height)
    background = Image.new('RGBA', target_shape, (4, 0, 0, 0,))
    for ind, img in enumerate(image_list):
        if img.mode != "RGBA":
            img = img.convert("RGBA")
        row, col = ind // number, ind % number
        location = (col * width, row * height)  # 放置位置
        background.paste(img, location)
    return background
image = image_concat(image_list,n)
plt.imshow(image)
plt.show()