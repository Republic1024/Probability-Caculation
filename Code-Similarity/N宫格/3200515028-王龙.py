import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import turtle
import random
import math

ix = Image.open("NIT.jpeg")
ix = np.array(ix)


# print(ix)
# plt.imshow(ix)
# plt.show()
def nj(n):
    m = int(math.sqrt(n))
    H, W = ix.shape[0], ix.shape[1]
    height = int(H / m)
    width = int(W / m)

    list1 = []
    for ih in range(0, H, height):
        for iw in range(0, W, width):
            t = ix[ih:ih + height, iw:iw + width, :]
            list1.append(t)

    random.shuffle(list1)
    # print(list1)
    # plt.imshow(list1)
    # plt.show()
    arr1 = np.array(list1)
    # for i in arr1:
    #     plt.imshow(i)
    #     plt.show()
    #     for i in range(n):
    #     result1 = np.hstack((arr1[0],arr1[1],arr1[2]))
    #     result2 = np.hstack((arr1[3],arr1[4],arr1[5]))
    #     result3 = np.hstack((arr1[6],arr1[7],arr1[8]))
    #     result= np.vstack((result1,result2,result3))

    list12 = []

    #     tuple1 = ()
    #     tuple2 = ()
    #     x = np.array(int(n)).reshape(m,m)
    for i in range(m):
        list11 = []
        for j in range(m):
            j2 = j + i * m

            list11.append(arr1[j2])

        list12.append(np.hstack(tuple(list11)))

    result = np.vstack(tuple(list12))
    #     array1 = np.array(list12)
    #     print(list13)
    #     results = np.vstack(np.array(list12))
    #     print(result)
    plt.imshow(result)
    plt.show()


n = int(input())
nj(n)
