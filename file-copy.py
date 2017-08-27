import os
import shutil
#filepath='\\\\ap-sha-dfs01\\China\\Shanghai\\Public\\PICs\\西藏照片\\'  #源文件目录
filepath='C:\\download\\'  #源文件目录
destpath='C:\\log\\'  #目标文件目录
targetnames=os.listdir(filepath)  #找出源文件中所有的文件
#print(targetnames)

#name='123.jpg'
x=0
count=0
for name in targetnames:  #获取源文件的所有文件名
    shutil.copyfile(filepath+name,destpath+name)  #copy到目标文件
    x+=1
    count+=x
    print('*'*10+'文件copy成功'+'*'*10+name)
    
print('所有文件copy成功,总数量%s'%x)

