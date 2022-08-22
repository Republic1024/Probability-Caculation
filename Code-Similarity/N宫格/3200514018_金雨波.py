import random
from PIL import Image
import matplotlib.pyplot as plt

def concat(list, number):
    image = list[0]
    width, height = image.size
    target_shape = (number * width, number * height)
    background = Image.new('RGBA', target_shape, (0, 0, 0, 0,))
    for ind, img in enumerate(list):
        if img.mode != "RGBA":
            img = img.convert("RGBA")
        row, col = ind // number, ind % number
        location = (col * width, row * height)
        background.paste(img, location)
    return background
image = Image.open('1.jpg')
num = int(input())
width, height = image.size
item_width = width // num
item_height = height // num
image.resize([(item_height * num), (item_width * num)])
list = []
for i in range(0, num):
    for j in range(0, num):
        box = (j*item_width,i*item_height,(j+1)*item_width,(i+1)*item_height)
        list.append(box)
imagelist = []
for box in list:
    imagelist .append(image.crop(box))
random.shuffle(imagelist)
image = concat(imagelist, num)
plt.imshow(image)
plt.show()