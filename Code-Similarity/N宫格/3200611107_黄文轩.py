import numpy
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from math import sqrt
import random

counts = sqrt(int(input("input: ")))
count = int(counts)
image = Image.open("img.png")
W, H = image.size
image = image.crop((0, 0, W - W % count, H - H % count))
W, H = image.size
image = numpy.array(image)
height = int(H / count)
width = int(W / count)
array = []
index = 1
for h in range(0, H, height):
    for w in range(0, W, width):
        tmp = image[h:h+height, w:w+width, :]
        array.append(tmp)
        index = index + 1
temp = []
random.shuffle(array)
for i in range(0, len(array), count):
    temp.append(np.concatenate(tuple(array[i:i+count]), axis=1))
plt.imshow(np.concatenate(tuple(temp), axis=0))
plt.show()