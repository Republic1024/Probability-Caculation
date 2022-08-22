import random
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from  cv2 import imwrite


number=eval(input("请输入你要裁剪的规格："))
#打开图像
image = Image.open("C19C15F5FAEEADC4E7C9EE326171D3E6.jpg")
# image = Image.open("C4B0047980D95E6F0A515BB56DFA449B.jpg")

image = np.array(image)
#图片的形式
print(image.shape)

#保存行数、列数
cols=image.shape[0]
rows=image.shape[1]

#根据输入的数进行裁剪
#记录列、行的余量：
cols_last=(cols%number)/2
rows_last=(rows%number)/2
#先进行整体的裁剪
cols_lower=int(cols_last)
cols_upper=int(cols-cols_last)
rows_lower=int(rows_last)
rows_upper=int(rows-rows_last)
print(cols_lower,cols_upper)
roi = image[cols_lower:cols_upper,rows_lower:rows_upper,:]
plt.imshow(roi)
plt.show()
# plt.imsave('test.jpg',roi)

cols_number=cols-cols%number
cols_number=cols_number/number
rows_number=rows-cols%number
rows_number=rows_number/number

imgs=[]
col_start=cols_lower
rows_start=rows_lower
count=0
for i in range(number):
    cols_lower = int(col_start + cols_number * i)
    for j in range(number):
        rows_lower=int(rows_start+rows_number*j)
        img = image[cols_lower:int(cols_lower+cols_number), rows_lower:int(rows_lower+rows_number),:]
        imgs.append(img)



lst = [i for i in range(number*number)]
random.shuffle(lst)
print(lst)

cnt1 = 0
cnt2 = 0
ls = []
i = 0
while i < number*number:
    ls2 = []
    for j in range(number):
        ls2.append(imgs[lst[i]])
        i += 1
    ls.append(ls2)

ls3 = []
for i in range(number):
    img = np.concatenate(ls[i], 1)
    ls3.append(img)
img = np.concatenate(ls3, 0)
imwrite("result.jpg", img)
