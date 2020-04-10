# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。

# list、tuple、dict、set、bytes、str虽然是Iterable，却不是Iterator。

#-------------------------------------
from typing import Iterable,Iterator

# Iterable
s = set('abcdefg')
type(s)
# <class 'set'>
isinstance(s,Iterable)
#True
isinstance(s,Iterator)
# False

it = iter(s)
it
# <set_iterator object at 0x0000000002484400>
isinstance(it,Iterator)
#True
isinstance(it,Iterable)
# True

#----------------------------------------
# Iterator对象表示的是一个数据流，
# Iterator对象可以被next()函数调用并不断返回下一个数据，
# Iterator 没有len()
# Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型

