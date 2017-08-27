#coding=utf-8

#第 0000 题:将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

from PIL import Image,ImageFont,ImageDraw  #由于PIL只支持到2.7版本，此处使用安装pillow库进行替代

def add_num(img):
    im=Image.open(img)
    w,h=im.size
    font=ImageFont.truetype('C:/WorkDay/Code/Python/MyPython/GitHub/verdanab.ttf')  #字体格式文件，参考C:\Windows\Fonts
    fillcolor='#ff0000'
    draw=ImageDraw.Draw(im)
    draw.text((w-50,80),'888',font=font,fill=fillcolor)
    im.save('r.jpg','jpeg')
    
if __name__=='__main__':
    add_num('1.jpg')
