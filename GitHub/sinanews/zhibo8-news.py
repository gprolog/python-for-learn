#-*-coding:utf-8-*-
import requests
from lxml import etree
import time
'''
#抓取直播吧中的新闻&比赛信息
url='https://www.zhibo8.cc/'
html=requests.get(url)
html=html.content
contentetree=etree.HTML(html)

print('*'*10+'basketbal-news'+'*'*10)
#抓取篮球相关的新闻
news=contentetree.xpath('.//*[@id="recommend"]/div[5]/ul/li')
for bk in news:
    #由于直播吧排版问题，使用两次抓取
    bknews=bk.xpath('a[1]/text()')
    bknews2 = bk.xpath('a[2]/text()')
    print(bknews[0])
    print(bknews2[0])
#抓取比赛结果信息
print('*'*10+'basketbal-game-news'+'*'*10)
gamenews=contentetree.xpath('.//*[@id="recommend"]/div[4]/ul/li')
for bkgame in gamenews:
    #获取文字内容
    bkgamenews=bkgame.xpath('a[1]/text()')
    #获取href
    bkgamenewshref = bkgame.xpath('a[1]/@href')
    bkgamenews2 = bkgame.xpath('a[2]/text()')
    bkgamenewshref2 = bkgame.xpath('a[2]/@href')
    print(bkgamenews[0])
    print(bkgamenewshref[0])
    print(bkgamenews2[0])
    print(bkgamenewshref2[0])
'''
'''
#抓取赛事直播信息
print('*'*10+'赛事直播信息'+'*'*10)
#.//*[@id='saishi108811']  使用xpath中的starts-with进行匹配（http://www.cnblogs.com/testlife007/p/6249039.html）
saishi=contentetree.xpath("//*[starts-with(@id,'saishi')]")
#可以使用这种方式提取href超链接
#saishihref=contentetree.xpath("//*[starts-with(@id,'saishi')]/a/@href")

for zhibo in saishi:
    #'text()'方式提出文字内容
    print(zhibo.xpath('text()')[0])
    #'@href'提出href
    print(zhibo.xpath('a/@href'))

'''
#获取篮球论坛中的热门帖子
#直播吧论坛中的帖子是异步加载的，解决办法参考下面信息
#https://segmentfault.com/q/1010000008885973/a-1020000008888194
#http://www.jianshu.com/p/da54149a0944
url2='http://bbs.zhibo8.cc/topic.html?tid=2090352'
luntan=requests.get(url2)
#time.sleep(20)
luntan1=luntan.content
tiezi=etree.HTML(luntan1)
tiezicontent=tiezi.xpath('/html/body/div[2]/div[3]/h1/text()')
#html/body/div[2]/div[6]/table/tbody[2]/tr[1]/td[1]/a[2]
print('tiezicontent',tiezicontent)
'''
for title in tiezicontent:
    titlecontent=title.xpath("/td[1]/a[2]/text()")
    print(titlecontent)
'''