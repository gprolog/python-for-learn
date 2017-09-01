#http://www.jianshu.com/p/288a92fc375a

import requests
from lxml import etree
html = requests.get(url='https://sports.sina.cn/nba/rockets/2015-10-07/detail-ifximrxn8235561.d.html?vt=4&pos=10')
html.encoding='utf-8'
html=html.content.decode('utf-8')
#print(html)

selector = etree.HTML(html)
title=selector.xpath('//h1[@class="art_title_h1"]/text()')
print('title:',title)
'''
content_field = selector.xpath('html/body/div[1]/div/table[5]/tbody/tr[1]/td[2]/table/tbody/tr/td')

print('content_field:',content_field)


#for each in content_field:
print('each:',each)
gongzi = each.xpath('//div[@class="job-primary"]/div[1]/h3/span')
gongsi = each.xpath('//div[@class="job-primary"]/div[2]/div/p/@name')
print('gongsi:',gongsi)
print('gongzi:',gongzi)

#print('each:',each)
for each in content_field:
    title = each.xpath('html/body/div[1]/div/table[5]/tbody/tr[1]/td[2]/table/tbody/tr/td/text()')
#gongsi = content_field.xpath('//div[@class="job-primary"]/div[2]/div/p/@name')
#print('gongsi:',gongsi)
    print('title:',title)
'''
