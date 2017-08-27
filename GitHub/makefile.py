#自动创建txt文件

import os
filepath='c:\\download\\file\\'
def makefile(s):
    if not os.path.isdir(filepath):  #判断目录是否存在
        os.mkdir(filepath)  #创建目录
        print('目录创建成功')
    for i in range(1,s+1):  #获取文件数量
        filename=str(i)+'.txt'  #获取文件名称规则
        openfile=open(filepath+filename,'ab')  ##a:以追加模式打开（必要时可以创建）append;b:表示二进制
        note=(b'my python test words,zhe shi wo yige yue de rizhi')   #要写入文件的字符串
        openfile.write(note)  #将字符串写入文件
        openfile.close()  #关闭文件
        print('文件写入成功，第%s个'%i)
if __name__=='__main__':
    s=int(input('请输入文件的数量:'))
    makefile(s)   #调用makefile函数

        
