#第 0010 题： 使用 Python 生成类似于下图中的字母验证码图片

from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

#随机字母
def rndChar():
    return chr(random.randint(65,90))

#随机颜色1
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

#随机颜色2
def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

#240X60

width=40*20
heigth=100
image=Image.new('RGB',(width,heigth),(255,255,255))
fontpath='C:\\WorkDay\\Code\\Python\\MyPython\\GitHub\\verdanab.ttf'  #样式文件路径
#创建Font对象
font=ImageFont.truetype(fontpath,66)
#创建Draw对象
draw=ImageDraw.Draw(image)

#填充每个像素
for x in range(width):
    for y in range(heigth):
        draw.point((x,y),fill=rndColor())

#输出文字
for i in range(4):
    draw.text((20*i*10,10),rndChar(),font=font,fill=rndColor2())

#模糊处理
image=image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')
