# 如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
# 函数作为返回值


def lazy_count(*args):

    def count():
        ax = 0
        for i in args:
            ax =ax+i
        return ax

    return count  #注意这里不能返回count() 有括弧就是要全部计算了

f = lazy_count(1,2,3,4,5,6,7,8,9,10)
# f
# type(f)
# <function lazy_count.<locals>.count at 0x000000000248ADC0>
# <class 'function'>
f()
# 55

# 当lazy_count返回函数count时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

#每次调用都会返回一个新的函数，即使传入相同的参数：
f0 = lazy_count(1,2,3,4,5,6,7,8,9,10)
f1 = lazy_count(1,2,3,4,5,6,7,8,9,10)

f0 ==f1
id(f)
id(f1)

#返回的函数实例不同  f1()和f2()的调用结果互不影响。

# 38317792
# 38317504

def count():
    fs = []
    for i in range(1, 4):  #这里调用一次count 就把四个一次计算完了
        def f():
             return i*i
        fs.append(f)
    return fs

x,y,z =count()
x()
y()
z()
# 结果不是期待的1 4 9
# 9
# 9
# 9
# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

#  返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

id(x)
id(y)
id(z)


# 38383040
# 38383184
# 38383328

# 如果要1 4 9就要函数使用时的输入时固定的
def  exe():
    def f(i):
        def g():
            return i*i
        return g

    x =[]
    for y in range(1,5):
        x.append(f(y))

    return x

f1,f2,f3 =exe()
f1()
f2()
f3()

#------------------------------------------------
# 作业

def  createCounter():
    def f(i):
        def g():
            return i+1
        return g

    x =[]
    for y in range(1,100):
        x.append(f(y))

    def h():
        next(iter(x))

    return h

def createCountera():

    i=[0]       #这里调用一次count,只计算一次

    def counter():

        i[0]=i[0]+1  #内层函数和外层函数里的局部变量不能通用，需要重新声明，或者用global、nonlocal之类的关键字声明 

        return i[0]

    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


