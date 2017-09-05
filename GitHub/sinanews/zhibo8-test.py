#for zhibo8 test
import requests
from lxml.html import  soupparser

url='http://bbs.zhibo8.cc/list.html?fid=8&page=1'
response=requests.get(url)
root=soupparser.fromstring(response.content)
start=root.xpath("html/body/div[2]/div[6]/table/tbody[2]/tr[1]/td[1]/a[2]/text()")
print(start)