#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import random
import math


# In[2]:


image_path = "picture.jpg"
img = np.array(Image.open(image_path))
plt.imshow(img)
img.shape


# In[3]:


def judge(img, x):
    
    w, h, _ = img.shape
    
    center_w = w//2
    center_h = h//2
    
    if w % x:
        w = (w // x) * x
    if h % x:
        h = (h // x) * x

    left_w = center_w - w//2 
    right_w = center_w + w//2
    left_h = center_h - h//2 
    right_h = center_h + h//2
    
    if w%2:
        right_w += 1
    if h%2:
        right_h += 1
        
    return left_w, right_w, left_h, right_h


# In[4]:


def crop_any(img):
    n = int(input())
    n = int(math.sqrt(n))
    
    left_w, right_w, left_h, right_h = judge(img, n)
    new_image = img[left_w:right_w, left_h:right_h, :]

    shape_w, shape_h, _ = new_image.shape

    patch_w, patch_h = shape_w // n, shape_h // n
    
    patch = []
    for w in range(0, shape_w, patch_w):
        for h in range(0, shape_h, patch_h):
            patch.append(new_image[w:w+patch_w, h:h+patch_h, :])
            
    random.shuffle(patch)
    
    img_list = []
    for i in range(0, len(patch), n):
        patch_list = [x for x in patch[i: i+n]]
        img_list.append(np.concatenate(patch_list, axis=0))
        
    new_img = np.concatenate(img_list, axis=1)
    plt.imshow(new_img)


# In[ ]:


crop_any(img)

