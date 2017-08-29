#test for github
class  people:
    name = ''
    age = 0
    _weight = 0
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self._weight = w
    def speak(self):
        print("%s 说：我%d岁。"%(self.name,self.age))
'''
#实例化类
p=people('runoob',10,30)
p.speak()
'''

#单继承示例
class student(people):
    grade=''
    def __init__(self,n,a,w,g):
        #调用父类的构造函数
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类方法
    def speak (self):
        print("%s说：我%d岁了，我在读%d年纪"%(self.name,self.age,self.grade))
'''
s=student('ken',9,60,4)
s.speak()
'''

#另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name= n
        self.topic=t
    def speaker(self):
        print("我叫%s，我是一个演说家，我的演讲主题是%s"%(self.name,self.topic))

#多重继承
class sample (speaker,student):
    a=''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)
test=sample("Tim",25,80,4,"Python")
test.speaker()
    
    

