#get title of peple dayly
#http://blog.csdn.net/jly58fgjk/article/details/51366524

import requests
import re
from bs4 import BeautifulSoup
from lxml import etree

url='http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000'
#header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
          #'Chrome/45.0.2454.101 Safari/537.36'}
html=requests.get(url)
html.encoding = 'UTF-8'
soup=(html.text,'html.parser')
page = re.findall('<li id=.*?>.*?<a href="(.*?)">.*?</a>',soup)     # 匹配不同目录后部分网址
i = 0

for each in page:
    #print (each)
    page1 ='http://www.liaoxuefeng.com'+each     #  不同目录前半部分+后半部分网址
    html2 = requests.get(page1)
    html2 = html2.text
    i +=1

for each2 in page1:
        Selector = etree.HTML(html2)
        content = Selector.xpath('//*[@class="x-wiki-content"]/p')   # 匹配汉字   是一个list
        for each2 in content:
            print (each2.text)
