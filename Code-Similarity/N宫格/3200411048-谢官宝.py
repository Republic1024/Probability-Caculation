import numpy as np
from PIL import Image


def divide(number, file_path, output):
    def preprocess(image):
        width, height = image.size
        cut_width = width % number
        cut_height = height % number

        s1 = cut_width // 2
        s2 = cut_width - s1
        s3 = cut_height // 2
        s4 = cut_height - s3

        # print(0,0,width, height)
        box = (s1, s3, width - s2, height - s4)
        # print(box)
        return image.crop(box)

    # 切图
    def cut_image(image):
        width, height = image.size
        item_width = width // number
        item_height = height // number
        box_list = []

        print((width % number, height % number))
        print("如果为(0, 0)证明图片分割没有残留")
        for i in range(0, number):
            for j in range(0, number):
                box = (j * item_width, i * item_height, (j + 1) * item_width, (i + 1) * item_height)
                box_list.append(box)

        image_list = [image.crop(box) for box in box_list]

        return image_list

    def image_concat(image_list, number):

        image = image_list[0]
        width, height = image.size
        target_shape = (number * width, number * height)
        background = Image.new('RGBA', target_shape, (0, 0, 0, 0))

        for ind, img in enumerate(image_list):
            if img.mode != "RGBA":
                img = img.convert("RGBA")
            # print(ind)
            row, col = ind // number, ind % number
            location = (col * width, row * height)  # 放置位置
            background.paste(img, location)

        return background

    image = Image.open(file_path)
    image = preprocess(image)  # 预处理
    image_list = cut_image(image)  # 切图
    print(image_list)
    np.random.shuffle(image_list)  # 打乱
    total = image_concat(image_list, number)  # 拼接
    total.show()
    total.save(output)  # 保存


n = int(input())
divide(n, "C:\\Users\\BGNP\\Desktop\\nit.jpg", "output_pic_5.png")
