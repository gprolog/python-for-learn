#-*-coding:utf-8-*-
#从高清网抓取首页的影片
import requests
from lxml import etree
import time

url='http://gaoqing.la/'
html=requests.get(url).text
time.sleep(8)
page=etree.HTML(html)
print(page)
film=page.xpath(".//*[@id='post_container']/li[1]/div/div[2]/h2/a")
print(film)

for newfilm in film:
    print(newfilm.xpath('text()'))
    print(newfilm.xpath('@href'))
