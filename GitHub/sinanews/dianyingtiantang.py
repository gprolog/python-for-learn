#-*-coding:utf-8-*-
#从电影天堂读取新片精品和必看热片
import requests
from lxml import etree
url='http://www.dy2018.com/'
html=requests.get(url).content
page=etree.HTML(html)
tiantangfilm=page.xpath(".//*[@id='header']/div/div[3]/div[4]/div[1]/div[2]/ul/li")

print('*'*20+'2017新片精品'+'*'*20)
for newfilm2017 in tiantangfilm:
    film2017=newfilm2017.xpath("a/text()")
    filmhref2017=newfilm2017.xpath("a/@href")
    print(film2017[0])
    print('http://www.dy2018.com/'+filmhref2017[0])

tiantangbikan=page.xpath(".//*[@id='header']/div/div[3]/div[4]/div[2]/div[2]/ul/li")
print('*'*20+'2017必看热片'+'*'*20)
for newfilmbikan in tiantangbikan:
    filmbikan2017=newfilmbikan.xpath("a/text()")
    filmhrefbikan2017=newfilmbikan.xpath("a/@href")
    print(filmbikan2017[0])
    print('http://www.dy2018.com/'+filmhrefbikan2017[0])