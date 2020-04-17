#---------------------------------------------------------
# 实例动态添加属性 
class Student(object):
    pass


s = Student()  
s.name = 'Micheal'  #动态添加属性
print(s.name)
# Micheal


#---------------------------------------------------------
# 实例动态添加方法，注意是实例不是类, 其他实例不会添加
def set_age(self,age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s)
# s.set_age(25)
# s.age
# 25

s2 = Student()
# s2.set_age(12)
# AttributeError: 'Student' object has no attribute 'set_age'

#---------------------------------------------------------
# 类动态添加方法

def set_score(self,score):
    self.score = score

Student.set_score = set_score   #带()就是None
s2.set_score(12)
# s2.score
# 12

#---------------------------------------------------------
# 限制实例添加属性  __slots__只对当前类的实例有显示，子类不限制

class Teacher(object):
    __slots__ = ('name','age')   #塞入

Teacher.name ='12'
Teacher.score = '80'
Teacher.name
Teacher.score

t = Teacher()
t.score
# '80'

# t.height =180
# t.height
# AttributeError: 'Teacher' object has no attribute 'height'


