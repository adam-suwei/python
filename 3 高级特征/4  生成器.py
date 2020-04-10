#-----------------------------------------------
# Python中，这种一边循环一边推算出后续的元素的机制，称为生成器：generator。
# 列表生成式的[]改成()，就创建了一个generator：  [] is list () is generator  list是平面 generator 是计算

#-----------------------------------------------
# 认识一下generator：
from typing import Iterable


g =(x*x for x in range(10))  #此时什么也不做，并不是把所有值都算出来存起来
g
type(g)
# <class 'generator'>

isinstance(g,Iterable)
# True


# <generator object <genexpr> at 0x0000000001DFEEB0>


#next() 计算下一个值--------------------------------
# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，
next(g)
next(g)
next(g)
next(g)

# 0
# 1
# 4
# 9

it = iter([1, 2, 3])
# 循环:
while True:
    try:
        # 获得下一个值:        
        x = next(it)
        print(x)
    except StopIteration:  #没有更多，抛StopIteration错误。
        print('--has no next()')
        # 遇到StopIteration就退出循环
        break

# 1
# 2
# 3
# --has no next()

#应该用for in代码简洁 避免StopIteration异常，--------------------------------
g = (x*x for x in range(4))
for i in g:
    print(i)
# 0
# 1
# 4
# 9

#著名的斐波拉契数列，除第一个和第二个数外，任意一个数都可由前两个数相加
def fib(max):
    if not isinstance(max,int):
        return '请输入整数！'
    n = 0
    a,b = 0,1
    while n <max:
        print('b=',b)
        n = n+1
        a,b = b,a+b
    return 'done'

# fib(5)
# b= 1
# b= 1
# b= 2
# b= 3
# b= 5
# 'done'

#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：

#generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
b=fib1(9)
next(b)
next(b)
next(b)
next(b)
next(b)
next(b)
next(b)
# 1
# 1
# 2
# 3
# 5
# 8
# 13

#------------------------------------------
# for 可以拿到yield 但是拿不到return 
for n in fib1(3):
    print(n)
# 1
# 1
# 2

#return 只在  StopIteration的value中
g = fib1(6)
while True:
    try:
        x = next(g)
        print('g=',x)
    except StopIteration as e:
        print(' 拿到return了：',e.value)
        break

# g= 1
# g= 1
# g= 2
# g= 3
# g= 5
# g= 8
#  拿到return了： done

#-----------------------------------------------------
# 作业
def triangles(n=1000):


    j = 1
    t =[0,1,0]

    while j <=n:
        if j ==1:
            yield [1]

        i= [x+t[y+1]  for y,x in enumerate(t) if y<len(t)-1]

        t =[0]
        t.extend(i)
        t.append(0)      
        j=j+1
        yield i

    return 'Done'

g = triangles(6)

# while True:
#     try:
#         x =next(g)
#         print('x =',x)
#     except StopIteration as e:
#         print (' return is:',e)
#         break

# x = [1]
# x = [1, 1]
# x = [1, 2, 1]
# x = [1, 3, 3, 1]
# x = [1, 4, 6, 4, 1]
# x = [1, 5, 10, 10, 5, 1]
# x = [1, 6, 15, 20, 15, 6, 1]
#  return is: Done

n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

