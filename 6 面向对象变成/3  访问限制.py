# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问

class Student(object):

    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name

    def get_score(self):
        if self.__score>=90:
            return 'A'
        elif self.__score>=60:
            return 'B'
        else:
            return 'C'

    def set_score(self,score):
        if 0 <= score <=100:
            self.__score = score
        else:
            raise ValueError('bad score')

bart = Student('xiaoA',88)
bart.__name   
# AttributeError: 'Student' object has no attribute '__name'
bart.get_name
# <bound method Student.get_name of <__main__.Student object at 0x00000000023F2580>>
bart.get_name()
# 'xiaoA'

bart.set_name('xiaoB')
bart.get_name()
# 'xiaoB'

# 相比较于变量暴露在外，getter setter 有了检查和清洗数据的管理能力
bart.set_score(88)
bart.get_score()
# B

bart.set_score(-10)
# ValueError: bad score

#_开头的表示：虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
# python会把__name 编辑成 _Student__name 仍然可以被访问
bart.set_name('private xiao')
bart._Student__name
bart.get_name()
# 'private xiao'

# 此时的__name 非内部__name 是bart实例新建的一个属性。
bart.__name ='test xiaoC'
bart.__name
# 'test xiaoC'


#---------------------------------------------------------
# 作业

class StudentB(object):
    def __init__(self,name,gender):
        self.__name = name 
        self.__gender = gender
    
    def get_name(self):
        return self.__name 
    def set_name(self,name):
        self.__name = name

    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        self.__gender = gender

# 测试:
bart = StudentB('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')