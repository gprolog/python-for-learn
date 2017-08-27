location='C:\\WorkDay\\Code\\Python\\MyPython\\CutePython\\cdays−3-test.txt'

def collect(file):
    result = {}   #  定义一个空字典
    for line in file.readlines( ):
        left,right = line.split( )
        if right in result :
            result[right].append(left)  #添加进列表
        else:
            result[right]=[left]        #如果字典中没有该值，那么新建一个Key
    return result

for key in collect(open(location,'r')).keys():
    print ('%d %s   =>   %s ' % (len(result[key]),key,result[key] ))
