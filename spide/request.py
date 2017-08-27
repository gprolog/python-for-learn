#登录百度个人中心

from urllib import request,parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
value={'username':'773779347@qq.com','password':'lpb1987'}  #用户名和密码建立字典
#context = ssl._create_unverified_context()
data=parse.urlencode(value).encode('UTF-8')#urlencode对字典值进行转换，生成a=1&b=2的格式（quote()函数对字符串进行转换）
print(data)

url='https://www.douban.com/accounts/login?source=music'

response=request.urlopen(url,data,20)
print(response.read())
