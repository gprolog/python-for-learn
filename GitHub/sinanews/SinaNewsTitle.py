#-*-coding:utf-8-*-
#参考http://blog.csdn.net/xiangwanpeng/article/details/56009423
import requests
import re
import os
from bs4 import BeautifulSoup

#新浪新闻地址
url='http://news.sina.com.cn/china/'

def getquip():
    html=requests.get(url)
    html.encoding = 'UTF-8'
    #使用剖析器html.parser
    soup=BeautifulSoup(html.text,'html.parser')
    with open('news.txt','w+') as f:
    #遍历每一个class=news-item的节点
        for news in soup.select('.news-item'):
            h2=news.select('h2')
            #只选择长度大于2的结果
            if len(h2)>0:
                #新闻时间
                time=news.select('.time')[0].text
                #新闻标题
                title=h2[0].text
                #新闻链接
                href=h2[0].select('a')[0]['href']
                #展示在屏幕上
                print(time,title,href)
				#写入文件
                f.write(time+title+href)
                f.write('\n')
        f.close()
      
if __name__=='__main__':
    print("Getting News ,please waiting a moment")
    getquip()
    print("Geting News complete,please look over the news.txt")

