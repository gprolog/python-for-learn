#-*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
import urllib
import time
import os
def getpic():
    url = 'https://www.zhihu.com/question/28085830/answer/232371279'
    html=requests.get(url).content
    time.sleep(5)
    soup=BeautifulSoup(html,'html.parser')
    links=soup.findAll('img')
    print('links',links)

    piclinks=[]
    print('---------开始获取图片---------')
    for link in links:
        print('it is in for loop')
        print('link',link)
        pic = link.get('src')
        print('pic',pic)
        piclinks.append(pic.split(' ')[0])
        # 判断目录是否存在，不存在的话创建目录
        if not os.path.exists('zhihuphoto'):
            os.makedirs('zhihuphoto')
        i=0
        for newpic in links:
            i+=1
            picpath='zhihuphoto\\'+str(i)+'.jpg'
            with open(picpath,'w'):
                urllib.request.urlretrieve(newpic,picpath)
        print('-------------图片下载完成-------------')



if __name__=='__main__':
    getpic()