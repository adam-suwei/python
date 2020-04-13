
#----------------------------------------------------------
# 类和实例
class Student(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s,%s' % (self.name,self.score))

bart = Student('a',19)  #调用时，不用传递self参数
bart  
Student

# >>> bart  这是个对象实例
# <__main__.Student object at 0x0000000000422880>
# >>> Student  这是个类
# <class '__main__.Student'>

bart.name = 'adam'
bart.name

# 'adam'


#----------------------------------------------------------
#数据封装, 封装内部逻辑

class Studt(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >=90:
            return 'A'
        elif self.score >=60:
            return 'B'
        else:
            return 'C'

lisb = Studt('adam',99)
print(lisb.name,lisb.get_grade)
# adam 99

# 类属性，在类方法外定义的属性。

# 实例属性，__init__内定义的属性。

# 类属性可以直接用类名访问，具有读写权限，也可以用实例名访问，但用实例访问时只能读。当实例访问类不存在的属性时，会在实例中新建属性。
bars = Studt('Bart',59)
bars.age = 8  #作为实例是可以再定义当前实例下的属性，类不会变化
bars.age
# 8

lisb.age #另一个实例里没有age
# AttributeError: 'Studt' object has no attribute 'age'

