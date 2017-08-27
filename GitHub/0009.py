#第 0009 题： 一个HTML文件，找出里面的链接。

#encoding=utf-8

import requests
from bs4 import BeautifulSoup

url='http://www.zhibo8.cc/'

data=requests.get(url)
soup=BeautifulSoup(data.text,'html.parser')
urls=soup.findAll('a')
for u in urls:
    print(u['href'])
