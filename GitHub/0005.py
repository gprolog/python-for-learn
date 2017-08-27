#第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

from PIL import Image
import os

path='c:\\download\\'
resultpath='c:\\picresult\\'
if not os.path.isdir(resultpath):#判断目录是否存在
    os.mkdir(resultpath)  #创建目录
for picname in os.listdir(path):  #listdir便利目录，返回文件名
    picpath=os.path.join(path,picname)  #join将路径和名称拼接
    print('picpath=',picpath)
    with Image.open(picpath)as im:  #打开文件
        w,h=im.size   #获取文件的长度和宽度
        n=w/1336 if (w/1336)>=(h/640) else h/640  #判断并设置
        im.thumbnail((w/n,h/n))  #thumbnail函数接受一个元组作为参数，分别对应着缩略图的宽高，在缩略时，函数会保持图片的宽高比例
        im.save(resultpath+'finish_'+picname.split('.')[0]+'.jpg','jpeg')  #保存修改分辨率的照片，并在文件名中加入finish_,并以.jpg结尾
