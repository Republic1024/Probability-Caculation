import random
from PIL import Image
import matplotlib.pyplot as plt
number = int(input())
image = Image.open('nit.jpg')
width, height = image.size
item_width = width//number
item_height = height//number
image.resize([(item_height*number),(item_width*number)])
box_list = []
for i in range(0,number):
    for j in range(0,number):
        box = (j*item_width,i*item_height,(j+1)*item_width,(i+1)*item_height)
        box_list.append(box)
image_list = []
for box in box_list:
    image_list.append(image.crop(box))
random.shuffle(image_list)
def image_concat(image_list, number):
    image = image_list[0]
    width, height = image.size
    target_shape = (number * width, number * height)
    background = Image.new('RGBA', target_shape, (0, 0, 0, 0,))
    for ind, img in enumerate(image_list):
        if img.mode != "RGBA":
            img = img.convert("RGBA")
        row, col = ind // number, ind % number
        location = (col * width, row * height)
        background.paste(img, location)
    return background
image = image_concat(image_list,number)
plt.imshow(image)
plt.show()