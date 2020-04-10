def tell():
    print(" test is here")

f=tell
tell()
f()

# test is here
# test is here

# 函数对象有一个__name__属性，可以拿到函数的名字：
tell.__name__
# 'tell'


# 不改now()，在函数调用前后自动打印日志
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# decorator就是一个返回函数的高阶函数.

def log(funct):
    def wraper(*args,**kw):
        print(' ------------ call %s ()-----------------' % funct.__name__)
        return funct(*args,**kw)
    return wraper

# @ log                              #@在交互模式下不行要执行文件才可以
def now():
    print('2020-4-1- 17:11')

# now()
#  ------------ call %s ()----------------- now  （加了@log基础上）
# 2020-4-1- 17:11
print('func name is ',now.__name__)
# func name is  wraper    #带@log情况下

# now()
#  ------------ call %s ()----------------- now  （加了@log基础上）
# 2020-4-1- 17:11
f=log(now)  #返回wrapper()函数
f()  #即在log()函数中返回的wrapper()函数
#  ------------ call %s ()----------------- now
# 2020-4-1- 17:11





