#父类方法
class Parent:
    def myMethod(self):
        print('调用父类方法')

#方法重写
class Child(Parent):
    def myMethod (self):
        print('调用子类方法')

c=Child()  #子类调用
c.myMethod()
