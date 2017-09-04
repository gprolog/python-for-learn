#从天天美剧抓取当日和当周的热片
from lxml import etree
import requests
import time

url = 'http://www.ttmeiju.com/'
html = requests.get(url).content
time.sleep(15)
page = etree.HTML(html)
hotweek = page.xpath(".//*[@id='wrapper']/div/div[2]/div[1]/ul/li[1]/div[2]/div/label[1]/a/text()")
hotday = page.xpath(".//*[@id='wrapper']/div/div[2]/div[3]/ul/li[1]/a/text()")
print(hotweek)
print(hotday)
