from selenium import webdriver
import urllib.request
from lxml import etree

#知乎首页所有的提问  因为要登录，需要操作cookie
url='https://www.zhihu.com/'
'''
driver=webdriver.PhantomJS()
driver.get(url)
#alltitle=driver.find_elements_by_xpath(".//*[@class='Button TopstoryItem-rightButton Button--plain']")
alltitle=driver.find_elements_by_xpath("//*[@class='QuestionItem-title']")
print(alltitle)
for title in alltitle:
    print(title.xpath('/a/text()'))
'''
html=urllib.request.urlopen(url).read().decode('utf-8')
page=etree.HTML(html)
title=page.xpath("/html/body/div[1]/div/div[1]/h2/text()")
print(title[0])