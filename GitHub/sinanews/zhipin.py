#-*-coding:utf-8-*-
#参考  http://www.cnblogs.com/xieqiankun/p/lxmlencoding.html
#http://www.jianshu.com/p/288a92fc375a

import requests
from lxml import etree
#抓取直聘网的公司 工资 工作主题
html = requests.get(url='https://www.zhipin.com/job_detail/?ka=header-job')
html=html.content.decode('utf-8')
selector = etree.HTML(html)
#print(selector)
#所以要抓取的信息在这个xpath下，先将此作为一个基点
content_field = selector.xpath('.//*[@id="main"]/div[3]/div[2]/ul/li')
for content_ex in content_field:
    #基于基点进一步抓取工作主题
    title = content_ex.xpath('div[1]/div[1]/h3/a/text()')
    #工资
    gongsi=content_ex.xpath('div[1]/div[2]/div/h3/a/text()')
    #公司
    gongzi = content_ex.xpath('div[1]/div[1]/h3/a/span/text()')

    print('title:',title[0])
    print('gongzi',gongzi[0])
    print('gongsi',gongsi[0])
    print('\n')
