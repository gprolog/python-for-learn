'''
第 0017 题： 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如

下所示：

<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!-- 
	学生信息表
	"id" : [名字, 数学, 语文, 英文]
-->
{
	"1" : ["张三", 150, 120, 100],
	"2" : ["李四", 90, 99, 95],
	"3" : ["王五", 60, 66, 68]
}
</students>
</root>
'''

import json
import xlwt
from collections import OrderedDict

filepath='C:\\WorkDay\\Code\\Python\\MyPython\\GitHub\\src\\'
textname='student.txt'
htmlname='student.xml'  #不需要创建excel文件，会自动创建

with open(filepath+textname,'r') as f:
    L=[]   #初始化列表L
    L.append(r"""   #在列表L中添加信息
<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!-- 
	学生信息表
	"id" : [名字, 数学, 语文, 英文]
-->
    """)
    L.append(f.read())  #继续在L末尾添加f中读取的数据
    L.append(r"""
</students>
</root>
    """)
    with open(filepath+htmlname,'w') as s:
        s.write(''.join(L))  #将L的内容写入到xml文件中
        
