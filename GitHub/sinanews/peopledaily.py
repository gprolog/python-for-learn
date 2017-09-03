
#-*-coding=utf-8-*-
'''
参考 
http://www.jianshu.com/p/2ae6d51522c3  
http://www.cnblogs.com/xieqiankun/p/lxmlencoding.html 
http://www.jianshu.com/p/288a92fc375a
'''
from lxml import etree
import requests
#要抓取内容的url地址
url='http://www.people.com.cn'
r=requests.get(url)
#这里是 GB2312。所以，只需要制定 encoding = apparent_encoding
r.encoding=r.apparent_encoding
#r=r.text #text属性返回的是Unicode类型数据，主要用于文在
#content属性返回的是二进制的数据，主要用于图片，在此处两者皆可
r=r.text
#使用etree.HTML()方法进行处理
contentTree=etree.HTML(r)
#通过xpath获取标题
title = contentTree.xpath('.//*[@id="rmw_a"]/div/h2/a/text()')
print (title)

#抓取要闻 实证 快讯
page=contentTree.xpath('.//*[@class="list14"]/li')
#print('page',page)

for a in page:
    tag_a=a.xpath('a/text()')
    print(tag_a)
