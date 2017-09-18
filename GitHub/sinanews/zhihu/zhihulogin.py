#https://github.com/xchaoinfo/fuck-login/blob/master/001%20zhihu/zhihu.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Required
- requests (必须)
- pillow (可选)
Info
- author : "xchaoinfo"
- email  : "xchaoinfo@qq.com"
- date   : "2016.2.4"
Update
- name   : "wangmengcn"
- email  : "eclipse_sv@163.com"
- date   : "2016.4.21"
'''
import requests
from lxml import etree
import time
from bs4 import BeautifulSoup
import os
import urllib
try:
    import cookielib
except:
    import http.cookiejar as cookielib
import re
import time
import os.path
try:
    from PIL import Image
except:
    pass


# 构造 Request headers
agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
headers = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    'User-Agent': agent
}

# 使用登录cookie信息
session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_discard=True)
except:
    print("Cookie 未能加载")


def get_xsrf():
    '''_xsrf 是一个动态变化的参数'''
    index_url = 'https://www.zhihu.com'
    # 获取登录时需要用到的_xsrf
    index_page = session.get(index_url, headers=headers)
    html = index_page.text
    pattern = r'name="_xsrf" value="(.*?)"'
    # 这里的_xsrf 返回的是一个list
    #_xsrf = re.findall(pattern, html)
    _xsrf='71203d197ae24d635cc78737fe539d11'
    return _xsrf

# 获取验证码
def get_captcha():
    t = str(int(time.time() * 1000))
    captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
    r = session.get(captcha_url, headers=headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)
        f.close()
    # 用pillow 的 Image 显示验证码
    # 如果没有安装 pillow 到源代码所在的目录去找到验证码然后手动输入
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
    captcha = input("please input the captcha\n>")
    return captcha


def isLogin():
    # 通过查看用户个人信息来判断是否已经登录
    url = "https://www.zhihu.com/settings/profile"
    login_code = session.get(url, headers=headers, allow_redirects=False).status_code

    if login_code == 200:
        return True
    else:
        return False


def login(secret, account):
    _xsrf = get_xsrf()
    headers["X-Xsrftoken"] = _xsrf
    headers["X-Requested-With"] = "XMLHttpRequest"
    # 通过输入的用户名判断是否是手机号
    if re.match(r"^1\d{10}$", account):
        print("手机号登录 \n")
        post_url = 'https://www.zhihu.com/login/phone_num'
        postdata = {
            '_xsrf': _xsrf,
            'password': secret,
            'phone_num': account
        }
    else:
        if "@" in account:
            print("邮箱登录 \n")
        else:
            print("你的账号输入有问题，请重新登录")
            return 0
        post_url = 'https://www.zhihu.com/login/email'
        postdata = {
            '_xsrf': _xsrf,
            'password': secret,
            'email': account
        }
    # 不需要验证码直接登录成功
    login_page = session.post(post_url, data=postdata, headers=headers)
    login_code = login_page.json()
    if login_code['r'] == 1:
        # 不输入验证码登录失败
        # 使用需要输入验证码的方式登录
        postdata["captcha"] = get_captcha()
        login_page = session.post(post_url, data=postdata, headers=headers)
        login_code = login_page.json()
        print(login_code['msg'])

    # 保存 cookies 到文件，
    # 下次可以使用 cookie 直接登录，不需要输入账号和密码
    session.cookies.save()

try:
    input = raw_input
except:
    pass
#获取登录后首页的内容
def getpage():
    pageurl='https://www.zhihu.com/'
    url1 = 'https://www.zhihu.com/question/23069403/answer/230022889'
    #使用url,cookies,headers获取首页内容
    html=requests.get(pageurl,cookies=session.cookies,headers=headers).content.decode('utf-8')
    #收到请求需要时间，延时
    time.sleep(5)

    page=etree.HTML(html)
    content = page.xpath(".//*[@class='content']")
    #print(content)
    for title in content:
        print('title',title.text)
        #将获取的信息写入文件zhihu.txt
        with open('zhihu.txt','w+') as f:
            #print('open the zhihu.txt')
            f.write(title.text[0])
            f.close()
    print('*'*10+'文件写入完成'+'*'*10)

    #构建BeaautifulSoup对象
    soup=BeautifulSoup(html,'html.parser')
    #获取html中'img'标签的对应值
    piccontent=soup.findAll('img')
    #定义一个列表，存放图片的link
    links=[]
    print('*'*10+'获取图片并保存到本地'+'*'*10)
    for piclink in piccontent:
        #获取'img'中的src连接
        pic=piclink.get('src')
        #将图片链接添加到links列表中
        links.append(pic.split(' ')[0])
        print(links)
        #判断目录是否存在，不存在的话创建目录
        if not os.path.exists('zhihuphoto'):
            os.makedirs('zhihuphoto')
        i=1
        for picnoe in links:
            i+=1
            #定义图片保存的目录+名称
            picname='zhihuphoto\\'+str(i)+'.jpg'
            with open(picname,'w'):
                #将图片保存
                urllib.request.urlretrieve(picnoe,picname)
    print('pic保存完成，保存目录zhihuphoto,保存数量%d'%i)

if __name__ == '__main__':
    if isLogin():
        print('您已经登录')
        getpage()

    else:
        account = input('请输入你的用户名\n>  ')
        secret = input("请输入你的密码\n>  ")
        login(secret, account)