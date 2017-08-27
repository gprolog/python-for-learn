
import sys
import imp
imp.reload (sys)
#sys.setdefaultencoding('utf8')

from urllib.request import urlopen
from urllib.request import urlretrieve
import urllib
import re

downpath='/download/'

def getHtml(url):
    page = urlopen(url)
    html = page.read()
    return url

def getImg(html):    
    reg = r'src="(.*?\.jpg)"'
#    html=html.decode('utf-8')
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)    
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve (imgurl,'%s.jpg' % x)
        x+=1
    
    return 

    with open (downpath,'wb') as f:
        f.write()
html = getHtml("http://tieba.baidu.com/p/4410942885")

print (getHtml(html))

