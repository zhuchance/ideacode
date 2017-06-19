#!/usr/bin/env python
# -*- coding: utf-8-*-

#一下三行代码是万能中文不乱码,但会触发一个bug,慎用
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

from PIL import Image
# import PIL
import math
import operator

def image_contrast(img1, img2):
    # 打开图片
    image1 = Image.open(img1)
    image2 = Image.open(img2)
    #
    h1 = image1.histogram()
    h2 = image2.histogram()

    result = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
    return result

if __name__ == '__main__':
    img1 = "./img1.jpg"  # 图片路径
    img2 = "./img2.jpg"
    contrastimg = image_contrast(img1,img2)
    print(contrastimg)