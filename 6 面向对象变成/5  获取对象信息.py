

#---------------------------------------------
# type()
# 返回的是具体的类 class：
type(123)
type('str')
# <class 'int'>
# <class 'str'>

type(abs)
a = list()
type(a)
# <class 'builtin_function_or_method'>
# <class 'list'>

type('abc') ==str
# True

import types
type(abs) == types.FunctionType
type(lambda x:x) == types.LambdaType
type(x for x in range(10)) ==types.GeneratorType
# True
# True
# True

#----------------------------------------------------
# isinstance()
# type 只能打印出当前类，isinstance可以判断多层父类 

class Animal(object):
    pass

class  Dog(Animal):
    pass

class Hasky(Dog):
    pass

a = Hasky()
type(a)
# <class '__main__.Hasky'>

#  总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
isinstance(a,Dog)
isinstance(a,Animal)
# True

#判断是否是某些类型中的一种
isinstance(123,(int,list,Animal))
# True

#---------------------------------------------
# dir() 
# 获得一个对象的所有属性和方法

dir('ABC')  
'ABC'.__dir__()  #等价

len('ABC')
'ABC'.__len__()   #等价 __len__
# 3

'ABC'.__len__
# <method-wrapper '__len__' of str object at 0x000000000

#---------------------------------------------
#  getattr()  setattr() hasattr()

class MyObject(object):
    def __init__(self):
        self.x =9
        self.__y =10
    def power(self):
        return self.x * self.x

#hasattr----------断存在属性和方法
obj = MyObject()  
hasattr(obj,'x')  
# True
hasattr(obj,'power')  
# True
hasattr(obj,'__y')
# False

#getattr----------获取属性和方法

def haspower(obj):
    if hasattr(obj,'power'):
        return obj.power()
    else:
        return None

haspower(obj)
# 81




getattr(obj,'x')
obj.__getattribute__('x') #等价
# 9
setattr(obj,'x',18)
obj.__setattr__('x',18) #等价
getattr(obj,'x')
# 18

fn = getattr(obj,'power')
type(fn)
# <class 'method'>
fn()
# 324   18*18

# 实例设置自己的属性
setattr(obj,'new','new set attr')
obj.new = 'new set attr'    #等价
obj.__getattribute__('new')
# 'new set attr'

# 获取属性'y'，如果不存在，返回默认值404
getattr(obj,'y',404)
# 404












