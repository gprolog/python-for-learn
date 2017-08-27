'''
第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：

{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
'''

import xlwt
import json
from collections import OrderedDict

filepath='C:\\WorkDay\\Code\\Python\\MyPython\\GitHub\\src\\'
textname='city.txt'
excelname='city.xls'


with open (filepath+textname,'r') as f:
    data=json.load(f,object_pairs_hook=OrderedDict)
    workbook=xlwt.Workbook()
    sheet1=workbook.add_sheet('city',cell_overwrite_ok=True)
    print(data)
    for index,(key,value) in enumerate (data.items()):
        print(index)
        print(key)
        print(value)
        sheet1.write(index,0,key)
        sheet1.write(index,1,value)
    workbook.save(filepath+excelname)
    print('excel写入成功')
