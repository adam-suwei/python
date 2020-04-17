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