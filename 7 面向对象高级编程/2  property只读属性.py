#----------------------------------------------------
# @property的装饰器 将方法变成属性，相当于getter
# @属性.setter 设置为方法为set方法
class Student(object):
    @property   #可以读，不可以写
    def score(self):
        return self._score

    @score.setter  # 设置可以写
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score muset be an integer! ')
        if value <0 or value>100:
            raise ValueError('score muset between 0 ~ 100!')
        self._score = value

    @property
    def age(self):
        return 70 - self._score


# score方法又可以直接访问，又被控制
s = Student()
s.score = 60
s.score
# 60
s.age= 10
# AttributeError: can't set attribute
s.age

# 1955


#----------------------------------------------------
# 作业


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        if value<=0:
            raise ValueError(' value must more than 0  !')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        if value<=0:
            raise ValueError(' height must more than 0 !')
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
