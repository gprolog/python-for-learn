#第 0013 题： 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)[http://tieba.baidu.com/p/2166231880]
#coding=utf-8
import os
import requests
from bs4 import BeautifulSoup
import re
'''
url='http://tieba.baidu.com/p/2166231880'
#url='http://tieba.baidu.com/p/5092951234?red_tag=c3273461198'
html=requests.get(url)
soup=BeautifulSoup(html.text,'html.parser')
img_urls=soup.findAll('img',bdwater='杉本有美吧,1280,860')
'''
url='http://tieba.baidu.com/p/4410942885'
html=requests.get(url)
soup=BeautifulSoup(html.text,'html.parser')
html.close()
#print('html',html)

img_urls=soup.findAll('img',class_="BDE_Image")
print('img_urls=',img_urls)
save_path="C:\\download\\"

for img_url in img_urls:
    img_src=img_url['src']
    print('img_src=',img_src)
    os.path.split(img_src)[1]
    

    with open('/download/'+os.path.split(img_src)[1],'wb') as f:
        print(os.path)
        f.write(requests.get(img_src).content)
        f.close()
     #   print(f)

