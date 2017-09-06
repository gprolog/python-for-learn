import requests
from lxml import etree
import urllib.request
import selenium.webdriver.support.ui as ui
from selenium import webdriver
#从知乎抓取热门回答
url='https://www.zhihu.com/question/64615364'
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
