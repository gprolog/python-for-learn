#第 0014 题： 纯文本文件 student.txt为学生信息如下,写入到excel中

'''
{
	"1":["张三",150,120,100],
	"2":["李四",90,99,95],
	"3":["王五",60,66,68]
}
'''

import xlwt
import json
from collections import OrderedDict

filepath='C:\\WorkDay\\Code\\Python\\MyPython\\GitHub\\src\\'
textname='student.txt'
excelname='student.xls'  #不需要创建excel文件，会自动创建
with open(filepath+textname,'r') as f:
    data=json.load(f,object_pairs_hook=OrderedDict)#第二个参数的作用：记住字段添加的顺序
    print(data)
    workbook=xlwt.Workbook()  #实例化workbook函数
    sheet1=workbook.add_sheet('shanghai',cell_overwrite_ok=True)##第二参数用于确认同一个cell单元是否可以重设值。
    
    for index,(key,values) in enumerate(data.items()):
    #enumerate对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
        print ('index=',index)
        print ('key=',key)
        print ('values=',values)
        sheet1.write(index,0,key)
        for i,value in enumerate(values):
            sheet1.write(index,i+1,value)
    workbook.save(filepath+excelname)
    print('写入成功')
#    f.close()

