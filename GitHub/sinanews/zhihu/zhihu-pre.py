from selenium import webdriver
import urllib.request
from lxml import etree
import requests
import re

#知乎首页所有的提问  因为要登录，需要操作cookie
#参考  http://www.cnblogs.com/puyangsky/p/5326384.html  https://www.zhihu.com/question/29925879

def getContent(url):
    #获取知乎首页内容
    r=requests.get(url)
    return r.content
    print('r.content',r.content)

#获取_xsrf标签的值
def getXSRF(url):
    content=str(getContent(url))
    pattern=re.compile('.*?<input type="hidden" name="_xsrf" value="(.*?)"/>.*?')
    match=re.findall(pattern,content)
    xsrf='71203d197ae24d635cc78737fe539d11'
    return xsrf
    print('xsrf',xsrf)

#登录
def login(baseurl,email,password):
    login_data={
        '_xsrf':getXSRF(baseurl),
        'password':password,
        'remember_me':'true',
        'email':email
    }
    #设置头信息
    '''
    headers_base={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
        'Host':'www.zhihu.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Referer':'https://www.zhihu.com/',
    }
    '''
    headers_base={
        'Referer': 'https://www.zhihu.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }
    #使用session登录，在接下来的访问中可以保留登录信息
    session=requests.session()
    print('session:',session)
    baseurl=url+'/login/email'
    #requests的session登录，以post方式，参数分别为url,headers,data
    content=requests.post(baseurl,headers=headers_base,data=login_data)
    print ('content.text',content.text)
    #再次使用session以get去访问知乎首页，一定要设置verity=False，否则访问失败
    s=session.get(url)
    print('s.text',s.text)

    #把爬下来的知乎首页写到文本
    f=open('zhihu.txt','w')
    f.write(s.text)

if __name__=='__main__':
    url = 'http://www.zhihu.com/'
    login(url,'773779347@qq.com','lpb1987')