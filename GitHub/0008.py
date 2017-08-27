#第 0008 题： 一个HTML文件，找出里面的正文。
#-*-coding:utf-8-*-

from bs4 import BeautifulSoup
import requests
import re

url='http://linyii.com/'

data=requests.get(url)
r=re.findall(r'<body>[\s\S]*</body>',data.text)
print(r[0])

print('-'*50)
soup=BeautifulSoup(data.text,'html.parser')
print(soup.body.text.encode('utf-8','ignore').replace('u\xa9','u'))
