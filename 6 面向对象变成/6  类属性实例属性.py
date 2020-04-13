class Student(object):
    count = 0   #这是类变量，相当于静态变量,各个实例都取这值。
    def __init__(self,name):
        self.name = name   #是实例变量，各个实例不同。
        Student.count =Student.count+1

       
s = Student('Adam')
s.age =18

hasattr(s,'name')
hasattr(s,'age')
# True
# True

#--------------------------------------------
# del 可以删除类属性和自定义属性
del s.name 
del s.age

hasattr(s,'name')
hasattr(s,'age')
# False
# False

Student.count
s.count
# 1
# 1

b =Student('a')
b =Student('b')

Student.count
s.count
b.count
# 3
# 3
# 3
#---------------------------------------------------------
# 作业
class StudentA(object):
    count = 0   #这是类变量，相当于静态变量,各个实例都取这值。
    def __init__(self,name):
        self.name = name   #是实例变量，各个实例不同。
        StudentA.count =StudentA.count+1


if StudentA.count != 0:
    print('测试失败!')
else:
    bart = StudentA('Bart')
    if StudentA.count != 1:
        print('测试失败!')
    else:
        lisa = StudentA('Bart')
        if StudentA.count != 2:
            print('测试失败!')
        else:
            print('Students:', StudentA.count)
            print('测试通过!')


