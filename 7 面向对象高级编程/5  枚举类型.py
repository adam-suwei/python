JAN = 1
FEB = 2
Mar = 3
...
Nov = 11
Dec = 12

from enum import Enum

Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
type(Month.Jan)
type(Month)
# <enum 'Month'>
# <class 'enum.EnumMeta'>

for name,member in Month.__members__.items():
    print (name,'=>',member,',',member.value)  #value属性则是自动赋给成员的int常量，默认从1开始计数。
# Jan => Month.Jan , 1
# Feb => Month.Feb , 2
# Mar => Month.Mar , 3
# Apr => Month.Apr , 4
# May => Month.May , 5
# Jun => Month.Jun , 6
# Jul => Month.Jul , 7
# Aug => Month.Aug , 8
# Sep => Month.Sep , 9
# Oct => Month.Oct , 10
# Nov => Month.Nov , 11
# Dec => Month.Dec , 12

from enum import Enum,unique
#@unique装饰器可以帮助我们检查保证没有重复值。
@unique  
class Weekday(Enum):
    Sun =0 
    Mon =1
    Tue =2
    Wed =3
    Thu =4
    Fri =5
    Sat =6

d1 = Weekday.Mon
print(d1)
print(Weekday['Mon'])
print(Weekday(1))
# Weekday.Mon
# Weekday.Mon
# Weekday.Mon

print(Weekday.Mon.value)
# 1


#--------------------------------------------
#作业
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    
    def __init__(self,name,gender):
        self.name = name
        if gender == Gender.Male or gender ==Gender.Female:
            self.gender = gender

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')