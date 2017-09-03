#-*-coding:utf-8-*-
#参考http://blog.csdn.net/xiangwanpeng/article/details/56009423
import requests
import re
import os
from bs4 import BeautifulSoup

#新浪新闻地址，测试抓取新浪体育新闻
url='http://sports.sina.com.cn/'

def getquip():
    html=requests.get(url)
    html.encoding = 'UTF-8'
    #使用剖析器html.parser
    soup=BeautifulSoup(html.text,'html.parser')
    with open('Sportsnews.txt','w+') as f:
        
    #遍历每一个class=news-item的节点
        for news in soup.select('.phdnews_hdline'):
            h2=news.select('h3')
            #只选择长度大于2的结果
            if len(h2)>0:
                #新闻时间
                #time=news.select('.time')[0].text
                #新闻标题
                title=h2[0].text
                #新闻链接
                href=h2[0].select('a')[0]['href']
                #展示在屏幕上
                print(title,href)
                    #写入文件
                f.write(title+'\n'+href)
                f.write('\n')
        f.close()
      
if __name__=='__main__':
    print("Getting News ,please waiting a moment")
    getquip()
    print("Geting News complete,please look over the news.txt")

