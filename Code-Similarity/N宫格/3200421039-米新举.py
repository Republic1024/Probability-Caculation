import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import sys


# 第一步：先将原图填充为正方形
def fill_image(image):
    width, height = image.size
    # 选取原图片长、宽中较大值作为新图片的九宫格半径
    new_image_length = width if width > height else height
    # 生产新图片【白底】
    new_image = Image.new(image.mode, (new_image_length, new_image_length), color='white')
    # 将原图粘贴在新图上，位置为居中
    if width > height:
        new_image.paste(image, (0, int((new_image_length - height) / 2)))
    else:
        new_image.paste(image, (int((new_image_length - width) / 2), 0))
    return new_image


# 第二步：将图片切割成九宫格
def cut_image(image, width, height, n=3):
    # 一行放3张图
    item_width = int(width / n)
    box_list = []
    index = 1
    for i in range(0, n):
        for j in range(0, n):
            # 确定四个坐标
            left = j * item_width
            upper = i * item_width
            right = (j + 1) * item_width
            lower = (i + 1) * item_width

            sub_image_array = image[upper:lower, left:right, :]  # 裁剪

            print(sub_image_array)  # 测试
            sub_image = Image.fromarray(sub_image_array)  # 生成子图像
            sub_image.save("./" + str(index) + ".jpg")  # 保存
            index += 1


if __name__ == '__main__':
    file_path = "./45.jpg"
    image = Image.open(file_path)
    image = fill_image(image)  # 居中，后面以白色背景填充,为了方便操作，不适用 numpy数组作为参数
    # print(np.array(image))  # 测试
    cut_image(np.array(image), image.width, image.height, n=4)  # n代表切割数量，默认为三