'''
.//*[@id='root']/div/main/div/div/div[1]/div[2]/div/div[3]/div/div[2]/h2/div/a
.//*[@id='root']/div/main/div/div/div[1]/div[2]/div/div[2]/div/div[3]/h2/div/a
.//*[@id='root']/div/main/div/div/div[1]/div[2]/div/div[1]/div/div[3]/h2/div/a
.//*[@id='root']/div/main/div/div/div[1]/div[2]/div/div[6]/div/div[2]/h2/div/a
'''
import requests
from lxml import etree
import urllib.request


url='https://www.zhihu.com/question/63798472'
html=urllib.request.urlopen(url).read()
#html=urllib.request.urlopen(url).read().decode("utf-8")
#html=requests.get(url).content
print(html)

page=etree.HTML(html)
print(page)
hottitle=page.xpath("//span[@class='RichText CopyrightRichText-richText']/text()")

print(len(hottitle))
