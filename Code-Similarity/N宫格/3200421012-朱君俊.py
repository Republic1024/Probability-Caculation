#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from skimage.io import imread,imshow
from PIL import Image


# In[2]:


im = imread("beautifulsheep.jfif")
plt.imshow(im)


# In[3]:


im.shape


# In[4]:


x,y= im.shape[0],im.shape[1]


# In[11]:


#length,width = map(int,input('输入目标长宽：').split())
n = int(input('拆分成n宫格: '))
width = int(x / sqrt(n))
length = int(y / sqrt(n))
num = int(sqrt(n))


# In[6]:


num


# In[12]:


#等宽切分
im_res = {}
im_width = np.split(im,range(0,y+1,length),axis = 1)
#imwidth = im_width[::-1]
for i in range(1,num+1):
    im_res[i] = np.split(im_width[i],range(0,x+1,width),axis = 0)
#等长切分
#im_length = np.split(im,range(0,x+1,length),axis = 0)
#imlength = im_length[::-1]


# In[13]:


imshow(im_width[2])


# In[14]:


plt.figure()
index = 1
for i in range(1,num+1):
    for j in range(1,num+1):
        plt.subplot(num,num,index)
        plt.imshow(im_res[i][j])
        plt.xticks([])
        plt.yticks([])
        index += 1
plt.show()


# In[89]:


#填充
color = [0,0,0]
im.fill(imlength,x,'b',alpha = 1.00)
im.fill(imwidth,y,'b',alpha = 1.00)


# In[ ]:




