#获取豆瓣的最新书评

#-*-coding:utf-8-*-

import requests
from bs4 import BeautifulSoup

#豆瓣书评地址
url='https://book.douban.com/review/latest/'

html=requests.get(url)
html.encoding = 'UTF-8'
soup=BeautifulSoup(html.text,'html.parser')
#已读写模式打开文件，若文件不存在则创建
with open ('douban-content.txt','w+') as f:
      #获取html中main-hd标签部分
      for news in soup.select('.main-hd'):
            #在main-hd标签部分中再获取title标签部分
            h2=news.select('.title')
            if len(h2)>0:
                  #获取书评时间，标签中main-meta为text的部分
                  time=news.select('.main-meta')[0].text
                  #获取书评的主题，h2[0]表示取h2中匹配到的第一个值
                  title=h2[0].text
                  #获取作者
                  author=news.select('.author')[0].text
                  #获取书评的主题
                  subtitle=news.select('.subject-title')[0].text
                  #获取简评
                  shtcont=soup.select('.short-content')[0].text
                  #获取书评的url地址
                  href=h2[0].select('a')[0]['href']
                  #输出到屏幕
                  print(time,title,author,subtitle,shtcont,href)
                  #写入文件
                  f.write(time+'\n'+'title'+title+'author'+author+'subtitle'+subtitle+'\n'+'shortcont'+shtcont+href)
                  f.write('\n'+'*'*80+'\n')
      f.close()
            
                  
                  
