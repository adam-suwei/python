# 函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量
# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
# 任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用
# Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。


# 函数式编程最重要的概念就是：组合；

# 一个函数只做一件事， 保证内部不被修改，且干净，无副作用，遵循开闭原则，然后将多个函数组合一起，便是简单的函数式编程范式；

# 简单实现
def plus(a, b):
    return a + b

def compose(func, array):
    return func(array[0], array[1])

result = compose(plus, [1, 2])
print(result)
f = plus
type(f)
# <class 'function'>  自建函数


#----------------------------------------------------------
# 变量可以指向函数
f = abs
f
type(f)
# <built-in function abs>  内建函数
# <class 'builtin_function_or_method'>

f(-10)
# 10


#----------------------------------------------------------
# 函数名也是变量
abs
# <built-in function abs>
abs=-10  
# 此时仅仅在本模块生效
# abs(-10) 
# TypeError: 'int' object is not callable

import builtins
builtins.abs =10
abs
#此时所有的模块都生效

#----------------------------------------------------------
#函数名作为参数传入函数

def add(f,x,y):
    return f(x)+f(y)

add(abs,-10,10)
# 20