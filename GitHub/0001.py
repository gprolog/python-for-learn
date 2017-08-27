'''
第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，
为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？
'''
from makefile import *   #从makefile中引用函数

import random
import string
filepath='/download/'
forselect=string.ascii_letters +string.digits   #生成字母（string.ascii_letters）+数字（string.digits）的随机数

def generate_code(count,length):
    file=open('/download/a.txt','w')  #已w方式打开文件  读写模式:r只读,r+读写,w新建(会覆盖原有文件),a追加,b二进制文件.常用模式
    for x in range(count):   #x循环控制激活码的数量
        Re=''
        for y in range(length):  #y循环控制激活码的长度
            Re+=random.choice(forselect)  #用random.choice返回随机数
        #Re=Re.encode('utf-8')
        print(Re)
        
        file.writelines(Re+'\n')
        print('写入成功')
    file.close()
       
if __name__=='__main__':
    generate_code(10,20)  #（个数，长度）
    #print(generate_code(10,20))
#    makefile(10)   #makefile中的makefile方法
