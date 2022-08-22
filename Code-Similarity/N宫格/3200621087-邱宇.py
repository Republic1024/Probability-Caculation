import numpy as np
import cv2 as cv
import math
import random


source = cv.imread("nit.jpg")
# cv.imshow("source", source)
# cv.waitKey(0)


# 原图的大小
# print (source.shape)
sourceRows = source.shape[0]
sourceColums = source.shape[1]

patchNum = eval(input())
patchSubNum = math.floor (math.sqrt(patchNum))
patchRows = sourceRows // patchSubNum
patchColums = sourceColums // patchSubNum
# print (patchRows)
# print (patchColums)

# print (list(range (0, sourceRows, patchRows)))
# print (list (range (0, sourceColums, patchColums)))

count = 1
patchList = []
for i in range (0, patchRows*patchSubNum, patchRows):
    for j in range (0, patchColums*patchSubNum, patchColums):
        patch = source[i:i+patchRows, j:j+patchColums]
        patchList.append(patch)
        cv.imwrite(f'output/patch{count}.jpg', patch)
        count += 1
        

# collage = np.concatenate (patchList, axis=0)
# cv.imshow('collage', collage)
# cv.waitKey(0)
# collage = np.ones (shape=(patchRows, patchColums*patchSubNum, 3))
# collage = np.zeros(shape=(0, 0, 3))
random.shuffle(patchList)

collageSubList = []
for i in range (0, patchNum, patchSubNum):
    collageSubList.append (np.concatenate(patchList[i:i+patchSubNum], axis=1))

collage = np.concatenate (collageSubList, axis=0)

cv.imwrite('output/collage.jpg', collage)

