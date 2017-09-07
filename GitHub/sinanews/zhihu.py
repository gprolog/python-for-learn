import requests
from lxml import etree
import urllib.request
import selenium.webdriver.support.ui as ui
from selenium import webdriver
from bs4 import BeautifulSoup
import os
import time
import re
#从知乎抓取某一条热门回答
#url='https://www.zhihu.com/question/64615364'
url='https://www.zhihu.com/question/64766695/answer/224184206'
'''
#1、使用requests库取不到文本内容，换成urllib.request.urlopen(url).read()这种方式
html=urllib.request.urlopen(url).read().decode('utf-8')
#html=requests.get(url).content
page=etree.HTML(html)
#print(page)
'''

#2、使用webdriver方法
driver=webdriver.PhantomJS()
driver.get(url)
#使用class类的方式抓取这一类下面的文本,使用element方法,注：使用element只匹配到的第一个
hottitle=driver.find_elements_by_xpath("//*[@class='RichText CopyrightRichText-richText']")
for alltitle in hottitle:
    print(alltitle.text)


#获取本页面上的图片
#参考 http://pmghong.blog.51cto.com/3221425/1334086/
save_path='C:/download/zhihu/'
html=str(urllib.request.urlopen(url).read())
img_re=re.compile(r'src="(.*?\.jpg)"')
img_list=img_re.findall(html)
print('img_list',img_list)
for i in range(len(img_list)):
    urllib.request.urlretrieve(img_list[i],save_path+'%s.jpg'%i)
print("picture download over")

