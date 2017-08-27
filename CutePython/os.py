#读取文件cdays−4-test.txt 内容，去除空行和注释行后，以行为单位进行排序，并将
#结果输出为cdays−4-result.txt。

# -*- coding: utf-8 -*-
import os


filepath='C:\\WorkDay\\Code\\Python\\MyPython\\CutePython\\'

with open(filepath+'cdays−4-test.txt','r') as f:
    if not os.path.isfile(filepath+'cdays−4-result.txt'):
        g=open(filepath+'cdays−4-result.txt','w')
        for lines in f:
            if len(lines)==1 or lines.startswith('#'):  #len(lines)判断行的长度（空行的长度为1）
                continue
            else:
                print(lines)         
                g.write(lines)
'''
                g.save()
                f.close()
                g.close()

        else:
            continue
'''
