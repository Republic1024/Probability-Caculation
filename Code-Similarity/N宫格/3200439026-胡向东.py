import random
from PIL import Image
import matplotlib.pyplot as plt
from time import perf_counter
import numpy as np

n = eval(input("请输入数字n代表n行:"))
m = eval(input("请输入数字m代表m列:"))

image = Image.open("nit.jpg")
image = np.array(image)
print(image.shape)
plt.imshow(image)

flag = 0
crop = 0
flag_Col = 0
height = image.shape[0]
width = image.shape[1]

remainder_row = image.shape[0] % n
remainder_col = image.shape[1] % m

if remainder_row != 0:
    delta_row = int(remainder_row / 2)
    if remainder_row % 2 == 0:
        image_crop_Row = np.split(image, range(0, height, 1), axis=0)
        image_crop_RowConnect = np.concatenate(image_crop_Row[delta_row:height - delta_row], axis=0)
    else:
        image_crop_Row = np.split(image, range(0, height, 1), axis=0)
        image_crop_RowConnect = np.concatenate(image_crop_Row[delta_row:height - delta_row - 1], axis=0)

    flag = 1
    crop = 1

if remainder_col != 0:
    delta_col = int(remainder_col / 2)
    if remainder_col % 2 == 0:
        if flag == 1:
            image_crop_Col = np.split(image_crop_RowConnect, range(0, width, 1), axis=1)  # 在width上进行裁剪
            image_crop_ColConnect = np.concatenate(image_crop_Col[delta_col:width - delta_col], axis=1)
        else:
            image_crop_Col = np.split(image, range(0, width, 1), axis=1)
            image_crop_ColConnect = np.concatenate(image_crop_Col[delta_col:width - delta_col], axis=1)

    else:
        if flag == 1:
            image_crop_Col = np.split(image_crop_RowConnect, range(0, width, 1), axis=1)  # 在width上进行裁剪
            image_crop_ColConnect = np.concatenate(image_crop_Col[delta_col:width - delta_col], axis=1)
        else:
            image_crop_Col = np.split(image, range(0, width, 1), axis=1)
            image_crop_ColConnect = np.concatenate(image_crop_Col[delta_col:width - delta_col], axis=1)
    crop = 1
    flag_Col = 1
if crop == 0:
    print("该图片不需要裁剪")
    plt.imshow(image)
else:
    if flag_Col == 0:
        plt.imshow(image_crop_RowConnect)
        print("该图片的大小为{}".format(image_crop_RowConnect.shape))
    else:
        plt.imshow(image_crop_ColConnect)
        print("该图片的大小为{}".format(image_crop_ColConnect.shape))

if flag == 1:
    image_crop_ColConnect = image_crop_RowConnect
if crop == 0:
    row_partition = np.split(image, range(0, height), axis=0)
else:
    row_partition = np.split(image_crop_ColConnect, range(0, height), axis=0)

ha = 0
hb = height // n
wa = 0
wb = width // m
fig, ax = plt.subplots(n * m, figsize=(30, 30))
cnt = 0
for i in range(n):
    row_partition_connect = np.concatenate(row_partition[ha:hb + 1], axis=0)
    for j in range(m):
        col_partirion = np.split(row_partition_connect, range(0, width), axis=1)
        col_partirion_connect = np.concatenate(col_partirion[wa:wb], axis=1)
        ax[cnt].imshow(col_partirion_connect)
        cnt += 1
        wa = wa + width // m
        wb = wb + width // m

    ha = ha + height // n
    hb = hb + height // n
    wa = 0
    wb = width // m
plt.tight_layout()

ha = 0
hb = height // n
wa = 0
wb = width // m
col_partirion_connect = []
for i in range(n):
    row_partition_connect = np.concatenate(row_partition[ha + 1:hb], axis=0)
    for j in range(m):
        col_partirion = np.split(row_partition_connect, range(0, width), axis=1)
        col_partirion_connect.append(np.concatenate(col_partirion[wa + 1:wb], axis=1))
        wa = wa + width // m
        wb = wb + width // m

    ha = ha + height // n
    hb = hb + height // n
    wa = 0
    wb = width // m

print("下面是分割的图像的大小：")
for i in range(n * m):
    print(col_partirion_connect[i].shape)

left = 0
right = m - 1

Total = []
index_list = [i for i in range(n * m)]
for i in range(n):
    index1 = random.choice(index_list)
    index_list.remove(index1)
    Combination = col_partirion_connect[index1]
    for i in range(m - 1):
        index2 = random.choice(index_list)
        Combination = np.concatenate((Combination, col_partirion_connect[index2]), axis=1)
        index_list.remove(index2)
    Total.append(Combination)
    left = left + m - 1
    right = right + m - 1

test = [i for i in range(n)]
indexT = random.choice(test)
Total_Combination = Total[indexT]
test.remove(indexT)
for i in range(n - 1):
    indexT1 = random.choice(test)
    Total_Combination_another = Total[indexT1]
    Total_Combination = np.concatenate((Total_Combination, Total_Combination_another), axis=0)
    test.remove(indexT1)

img = Image.fromarray(Total_Combination)
plt.imshow(img)