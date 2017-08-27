'''
第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

[
	[1, 82, 65535], 
	[20, 90, 13],
	[26, 809, 1024]
]
'''



import xlwt
import json
from collections import OrderedDict


filepath='C:\\WorkDay\\Code\\Python\\MyPython\\GitHub\\src\\'
textname='numbers.txt'
excelname='numbers.xls'


with open (filepath+textname,'r') as f:
    data=json.load(f,object_pairs_hook=OrderedDict)

    print(data)
    workbook=xlwt.Workbook()
    sheet1=workbook.add_sheet('city',cell_overwrite_ok=True)

    for row,number_arr in enumerate (data):
        print('row=',row)
        print('number_arr',number_arr)
        for col,number in enumerate(number_arr):
            print('col=',col)
            print('number=',number)
            
    sheet1.write(row,col,number)
    workbook.save(filepath+excelname)
    f.close()
    print('excel写入成功')
    
