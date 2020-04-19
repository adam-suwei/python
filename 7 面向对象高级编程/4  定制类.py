#----------------------------------------------------
# class 中的 __str__

class Student(object):
    def __init__(self,name):
        self.name = name
    

    def __str__(self):
        return ('hi~ I am a student ,my name is: %s' % self.name)

    __repr__ = __str__

s = Student('a gang')
print(s)
# hi~ I am a student ,my name is: a gang
s
# 直接显示变量调用的不是__str__()，而是__repr__()
#  haha ! I am a student ,my name is a gang
# __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。

#----------------------------------------------------
# class 中的 __iter__

class Fib(object):
    def __init__(self):
        self.a,self.b =0,1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b,self.a+self.b
        if self.a>10000:
            raise StopIteration
        return self.a

for n in Fib():
    type(n)
    print(n)

#----------------------------------------------------
# __getitem__ 根据下标获取数据

class Fia(object):
    def __getitem__(self,n):
        a,b = 1,1
        for x in range(n):
            a,b =b,a+b
        return a
f = Fia()
f[9]
# 55


class Fic(object):
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b =1,1       
            for x in range(n):
                a,b =b,a+b
            return a
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b = 1,1
            L =[]
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b,a+b
            return L

fc = Fic()
fc[9]
# 55
l = fc[1:10]
l
# [1, 2, 3, 5, 8, 13, 21, 34, 55]

#----------------------------------------------------
#__setitem__()   __delitem__()
# _getattr__ 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，

class Sta(object):
    def __init__(self):
        self.name = 'Micheal'

    def __getattr__(self,attr):
        if attr == 'score':
            return 99
        elif attr =='name':
            return 'adam'
        elif attr == 'age':
            return lambda:25  #注意这是一个方法
        raise AttributeError('\'Sta\' object has no attribute \'%s\'' %attr) #没有这样则返回None

s = Sta()
s.name  #找到了name属性就不走getattr方法了
s.score 
s.age() 
# 'Micheal'
# 99
# 25
s.height
# 'Sta' object has no attribute 'height'


#----------------------------------------------------
# 把对象当成方法调用 这么一来，我们就模糊了对象和函数的界限
class Studena(object):
    def __init__(self,name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Studena('adam')
s()

#callable 判断是否是函数
callable(Studena('a'))
# True
callable(range(10))
# False
