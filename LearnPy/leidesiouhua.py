'''
#类的私有属性
class justCounter:
    __secretCount=0  #私有变量
    publicCount=0  #公开变量

    def count(self):
        self.__secretCount +=1
        self.publicCount+=1
        print(self.__secretCount)

counter=justCounter()
counter.count()
counter.count()
print(counter.publicCount)
print(counter.__secretCount)
'''

#类的私有方法
class Site:
    def __init__ (self,name,url):
        self.name=name  #公有属性
        self.__url=url #私有属性
    def who (self):
        print('name:',self.name)
        print('url:',self.__url)
    def __foo(self):  #私有方法
        print('这是私有方法')
    def foo(self):  #公共方法
        print('这是公有方法')
        self._foo()

x=Site('菜鸟教程','www.baidu.com')
x.who()
x.foo()
x.__foo()
