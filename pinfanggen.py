'''
#计算平方根
import cmath  #导入复数数学模块
num=float(input("请输入一个数字"))
num_sqrt=cmath.sqrt(num)
print('{0}的平方根是{1:3f}'.format(num,num_sqrt.real))
'''


'''
#求解二次方程
#ax**2+bx+c=0

import cmath

a=float(input('请输入a:'))
b=float(input('请输入b:'))
c=float(input('请输入c:'))

#计算
d=(b**2)-(4*a*c)

x1=(-b+cmath.sqrt(d))/(2*a)
x2=(-b-cmath.sqrt(d))/(2*a)

print('方程的两个解分别为{0}和{1}'.format(x1,x2))
'''
'''
#计算三角形面积
#三角形面积的海伦公式 S=sqrt(P(P-A)(P-B)(P-C))  P=(A+B+C)/2
import cmath

A=float(input("请输入第一条边的长度:"))
B=float(input("请输入第二条边的长度:"))
C=float(input("请输入第三条边的长度:"))

P=(A+B+C)/2

area=cmath.sqrt(P*(P-A)*(P-B)*(P-C))

print('这个三角形的面积为：{0:.3f}'.format(area.real))
'''

'''
#生成随机数
import random
#每次运行都会产生一个0-9的随机数
print(random.randint(0,9))
'''

'''
#摄氏温度转到华氏温度F=C*1.8+32

C=float(input('请输入摄氏温度'))
F=C*1.8+32
print('摄氏温度{0}对应的华氏温度是{1}：'.format(C,F))
'''
'''
#变量交换
#方法1：使用临时变量temp
a=int(input('请输入整数a的值\t'))
b=int(input('请输入整数b的值\t'))

#定义一个中间变量temp
temp=a;
a=b;
b=temp;

print("交换后a的值为{0},b的值为{1}".format(a,b))


#方法2：不使用临时变量
a,b=b,a
'''

'''
#If语句

num=float(input('请输入一个数字:'))
if num>0:
    print('是一个正数')
elif num==0:
    print('是个0')
else:
    print('是个负数')
'''

#python判断字符串是否为数字
'''
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError,ValueError):
        pass
    return False

#测试字符串和数字
print (is_number('foo'))
'''

#判断数字是奇数还是偶数
'''
num=int(input('请输入一个数字：'))
if (um%2)==0:  #取余
    print('{0}这是个偶数'.format(num))
else:
    print('{0}这是个奇数'.format(num))
'''

#判断闰年
'''
year=int(input('请输入年份：'))
if ((year%4==0)and (year%100!=0))or (year%400==0):
     print('{0}这一年是闰年'.format(year))
else:
    print('{0}这一年不是闰年'.format(year))
'''

#获取最大数
'''
num=(29,43,2,11,88,43)

print('元组中最大的数为：',max(num))
'''

#判断质数
'''
num=int(input('请输入一个数字:'))

if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print(num,'不是质数')
            print(num,'等于',i,'乘以',num//i)
            break
    else:
            print(num,'是质数')
else :
    print(num,'不是质数')
'''

#输出某个区间内的素数
'''
lower=int(input('输入区间的上限:'))
upper=int(input('输入区间的下限:'))

for num in range(lower,upper+1):
    if num>1:  #素数大于1
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)
'''

#阶乘
'''
n=int(input('请输入要计算阶乘的数：'))
total=1 #生命变量total,用来计算阶乘
if n==0:
    print('0的阶乘为1')
elif n<0:
    print('负数没有阶乘')
else:
    for i in range(1,n+1):
        total=total*i
    print(n,'的阶乘为：',total)
'''

#九九乘法表
'''
for i in range(1,10):
    for j in range (1,i+1):
        print('{0}X{1}={2}\t'.format(i,j,i*j),end='')
    print()
'''

#斐波纳妾数列
'''
num=int(input('你需要几项数列：'))

n1=0
n2=1
count=2
if num<=0:
    print('请输入一个正整数')
elif num==1:
    print('数列为：',n1)
else:
    print('数列为：')
    print(n1,',',n2,end=',')
    while count<num:
        nth=count+num
        print(nth,end=',')
        #更新值
        n1=n2
        n2=nth
        count+=1
'''

#阿姆斯特朗数  如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数
'''
num=int(input('请输入一个数值：'))
n=len(str(num))  #获取num的位数（只有str类型才能使用len方法）

sum=0  #初始化num n次方的综合
temp=num
while temp>0:
    a=temp%10
    sum+=a**n
    temp=temp//10

if num==sum:
    print(num,'是阿姆斯特朗数')
else:
    print(num,'不是阿姆斯特朗数')
'''


#获取某个区间的所有阿姆斯特朗数
'''
lower=int(input('请输入下限:'))
upper=int(input('请输入上限:'))

for num in range(lower,upper+1):
    n=len(str(num))
    sum=0  #初始化num n次方的综合
    temp=num
    while temp>0:
        a=temp%10
        sum+=a**n
        temp=temp//10
    if num==sum:
       print(num)
    
'''

#进制转换
'''
dec=int(input('输入数字：'))
print('十进制数为：',dec)
print('二进制数为：',bin(dec))
print('十六进制为：',hex(dec))
print('八进制为：',oct(dec))
'''

#ASCII码与字符相互转换
'''
c=input('请输入一个字符')

a=int(input('请输入一个ASCII码'))

print(c,'对应的ACSCII码为：',ord(c))

print(a,'对应的字符为：',chr(a))
'''

#求两个数的最大公约数
'''
def htc(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if(x%i==0)and (y%i==0):
            htc=i
    return htc
num1=int(input('请输入第一个数'))
num2=int(input('请输入第二个数'))

print(num1,'和',num2,'的最大公约数为：',htc(num1,num2))
'''

#求两个数的最小公倍数
'''
def lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while(True):
        if(greater%x==0)and (greater%y==0):
            lcm=greater
            break
        greater+=1
    return lcm
num1=int(input('请输入第一个数'))
num2=int(input('请输入第二个数'))

print(num1,'和',num2,'的最小公倍数为：',lcm(num1,num2))
'''

#简单计算器的实现
'''
#num=0
def add(x,y):
    #相加
    return x+y
def subtract(x,y):
    #相减
    return x-y
def mutiply(x,y):
    #乘法
    return x*y
def divide(x,y):
    #除法
    return x/y
#def numget():
num=int(input('请选择运算：\n1、加法\n2、减法\n3、乘法\n4、除法\n'))
a=int(input('请输入第一个数字:'))
b=int(input('请输入第二个数字:'))
    
#numget()

while (num):
    if num==1:
        print(a,'+',b,'=',add(a,b))

    elif num==2:
        print(a,'-',b,'=',subtract(a,b))
    elif num==3:
        print(a,'*',b,'=',mutiply(a,b))
    elif num==4:
        print(a,'/',b,'=',divide(a,b))
    else:
        print('非法输入')
    num=int(input('请选择运算：\n1、加法\n2、减法\n3、乘法\n4、除法\n'))
    a=int(input('请输入第一个数字:'))
    b=int(input('请输入第二个数字:'))
'''

#生成日历
'''
import calendar

yy=int(input('请输入年份:'))
mm=int(input('请输入月份:'))

#显示日历
print(calendar.month(yy,mm))
'''

#使用递归斐波纳妾数列
'''
def recur_fibo(n):

#    递归函数
#    输出斐波纳妾数列

    if n<=1:
        return n
    else:
        return (recur_fibo(n-1)+recur_fibo(n-2))
num=int(input('您要输出几项:'))
if num<=0:
    print('请输入正整数')
else:
    print('斐波纳妾数列:')
    for i in range (num):
        print(recur_fibo(i))
'''

#文件IO
'''
with open('test.txt','wt') as outfile:
    outfile.write('这是写入文件的部分\n正常情况下能看到')
with open('test.txt','rt') as infile:
    text=infile.read()
print(text)
'''

#大小写转换
'''
str='www.baidu.com'
print(str.upper())#转换为大写
print(str.lower())#转换为小写
print(str.capitalize())#首字母转换为大写
print(str.title())#每个单子的首字母转换为大写
'''

#计算每个月的天数
'''
import calendar
monthRange=calendar.monthrange(2016,9)
print(monthRange)
'''

#获取昨天日期
import datetime
def GetYesterday():
    today=datetime.date.today()#获取当天时间
    oneday=datetime.timedelta(days=1)#获取一天时间
    yesterday=today-oneday
    return yesterday
print(GetYesterday())
    
