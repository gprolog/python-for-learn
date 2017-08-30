#for get news from mew.163.com

#-*-coding:utf-8-*-

import requests
from bs4 import BeautifulSoup

url='http://news.163.com/domestic/'

html=requests.get(url)
html.encoding = 'UTF-8'
soup=BeautifulSoup(html.text,'html.parser')

with open ('163news.txt','w+') as f:
      print('is with')
      for news in soup.select('.news_title'):
            print('news',news)
            h2=news.select('h3')
            #print('h2:',h2)
            if len(h2)>0:
                  time=news.select('.time')[0].text
                  title=h2[0].text
                  href=h2[0].select('a')[0]['href']
                  print(time,title,href)
                  f.write(time+title+href)
                  f.write('\n')
      f.close()
            
                  
                  
