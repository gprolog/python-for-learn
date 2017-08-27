#-*- coding:utf-8 -*-
import os
import sys
location='C:\\WorkDay\\Code\\Python\\MyPython\\CutePython\\cdays−3-test.txt'
#print sys.argv()
def collect(filepath):
    result={}
    for line in filepath.readlines():
        left,right=line.split()
        if right in result:
            result[right].append(left)
        else:
            result[right]=[left]
    return result
#collect(open(location,'r'))
#    print ("%d '%s'\t=>\t%s" % (len(left), right, left))
'''
for key in collect(open(location,'r')).keys():
    print (('%d %s => %s') % len(result[key]),key,result[key])
    
    #print(result)
'''
if __name__=='__main__':
    result=collect(open(location,'r'))
    for (right,lefts) in result.items():
        print("%s '%s'\t=>\t%s"%(len(lefts),right,lefts))
        
        
        
