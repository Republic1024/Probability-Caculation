from PIL import Image
import glob
import numpy as np
from cv2 import imread,imwrite
import sys
#先将 input image 填充为正方形
def fill_image(image):
  width, height = image.size
  #选取长和宽中较大值作为新图片的
  new_image_length = width if width > height else height
  #生成新图片[白底]
  new_image = Image.new(image.mode, (new_image_length, new_image_length), color='white')  #注意这个函数！
  #将之前的图粘贴在新图上，居中
  if width > height:#原图宽大于高，则填充图片的竖直维度 #(x,y)二元组表示粘贴上图相对下图的起始位置,是个坐标点。
    new_image.paste(image, (0, int((new_image_length - height) / 2)))
  else:
    new_image.paste(image, (int((new_image_length - width) / 2),0))
  return new_image
def cut_image(image):
  width, height = image.size
  item_width = int(width / 3) #因为朋友圈一行放3张图。
  box_list = []
  # (left, upper, right, lower)
  for i in range(0,3):
    for j in range(0,3):
      #print((i*item_width,j*item_width,(i+1)*item_width,(j+1)*item_width))
      box = (j*item_width,i*item_width,(j+1)*item_width,(i+1)*item_width)
      box_list.append(box)
  image_list = [image.crop(box) for box in box_list]
  return image_list
#保存
def save_images(image_list):
  index = 1
  for image in image_list:
    image.save(str(index) + '.png', 'PNG')
    index += 1
if __name__ == '__main__':
  file_path = "2.jpg" #图片保存的地址
  image = Image.open(file_path)
  #image.show()
  image_new = fill_image(image)
  image_list = cut_image(image_new)
  save_images(image_list)
imgs,heights,widths = [],[],[]
for f in glob.glob("pictures/*.png"):
    img = imread(f,-1)
    h,w = img.shape[:2]
    heights.append(h)
    widths.append(w)
    imgs.append(img)
img0 = np.concatenate(imgs[:3],0)           #沿1轴横向拼接
img1 = np.concatenate(imgs[3:6],0)
img2 = np.concatenate(imgs[6:],0)
img9 = np.concatenate([img0,img1,img2],1)   #沿0轴纵向拼接
imwrite("3x3_0.jpg",img9)
