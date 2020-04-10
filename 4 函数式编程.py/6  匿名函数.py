

list(map(lambda x: x*x,list(range(10))))


#匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
f = lambda x:x*x
f(8)

#匿名函数作为写返回值
def fl(x):
    return lambda x:x*x

y=fl(7)
y(7)


#----------------------------------------
# 改造 is_odd
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, range(1, 20)))
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

list(filter(lambda x:x%2==1,range(1,20)))
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]