# functools.partial就是帮助我们创建一个偏函数的，不用编写代码就可以建立对一个方法参数的再次定义

import functools
int2 = functools.partial(int,base=2)

int2('10')
int2('101')
int2('101',base=10)


# 2
# 5
# 101

# 创建偏函数时，实际上可以接收[函数对象]、[*args]和[**kw]这3个参数，

# 固定了int()函数的关键字参数**kw  base
int3 = functools.partial(int, base=2)
int3('10010')
# 相当于：
kw = { 'base': 2 }
int('10010', **kw)
# 18


# 实际上会把10作为*args的一部分自动加到左边，也就是
max2 = functools.partial(max,10)
max2(2,3,4)
max(10,2,3,4)
# 相当于：
args = (10, 5, 6, 7)
max(*args)
# 10