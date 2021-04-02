import os

from PIL import Image
import numpy

if __name__ == '__main__':
    in_file_path = input("输入文件位置:")
    # 打开图片，并转换为灰度图
    img_in = Image.open(in_file_path).convert("L")
    # 转换为数组
    in_array = numpy.array(img_in)
    shape = in_array.shape
    width = shape[1]
    height = shape[0]
    # 初始化输出图片数组
    out_array = numpy.zeros((height, width, 4))
    # 遍历像素
    for h in range(0, height):
        for w in range(0, width):
            # 获取灰度
            grey = in_array[h, w]
            # 像素设置为黑色，并反转灰度作为透明度
            out_array[h, w] = (0, 0, 0, 255 - grey)
    # 输出的图片
    img_out = Image.fromarray(numpy.uint8(out_array))
    # 保存图片
    img_out.save(in_file_path[:in_file_path.rindex(".")] + "_alpha.png", "png")
