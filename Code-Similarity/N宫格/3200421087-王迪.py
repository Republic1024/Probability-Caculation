import random
import numpy as np
import cv2

img = cv2.imread('06.png')
img = cv2.resize(img, (int(img.shape[0] / 10) * 3, int(img.shape[0] / 10) * 3))

nums = random.sample(range(0, 3), 3)
nums.extend(random.sample(range(3, 6), 3))
nums.extend(random.sample(range(6, 9), 3))

h = int(img.shape[0] / 3)
w = int(img.shape[1] / 3)

index = 0

imgs = []
index = 0
for i in range(0, 3):
    for j in range(0, 3):
        imgs.append(img[i * h: (i + 1) * h, j * w: (j + 1) * w, :])

img0 = imgs[0]
img0 = np.hstack((img0, imgs[1]))
img0 = np.hstack((img0, imgs[2]))
img1 = imgs[3]
img1 = np.hstack((img1, imgs[4]))
img1 = np.hstack((img1, imgs[5]))
img2 = imgs[6]
img2 = np.hstack((img0, imgs[7]))
img2 = np.hstack((img0, imgs[8]))



img1 = cv2.resize(img1, (img0.shape[1], img0.shape[0]))
img2 = cv2.resize(img2, (img0.shape[1], img0.shape[0]))

print(img0.shape)
print(img1.shape)
print(img2.shape)

img = np.vstack((img0, img1))
img = np.vstack((img, img2))

cv2.imshow('img', img)
cv2.waitKey(0)
