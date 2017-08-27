#第 0021 题： 通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。
import os
from hashlib import sha256
from hmac import HMAC

def encypt_password(password,salt=None):
    if salt is None:
        salt=os.urandom(8) #64bit
        
    if isinstance (salt,str):
        salt=salt.encode(encoding='utf-8')
        print('salt=',salt)

    #assert 8==len(salt)  #assert 断言
    #assert isinstance(salt,str)

    #password=password.decode()
    
    result=password.encode(encoding='utf-8')
    print('result=',result)
    for i in range(10):
        result=HMAC(result,salt,sha256).digest()

    return salt+result

if __name__=='__main__':
    hashed=encypt_password('123')
    print(hashed)
