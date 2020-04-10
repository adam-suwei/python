def log(funct):
    def wraper(*args,**kw):
        print(' ------------ call %s ()-----------------' % funct.__name__)
        return funct(*args,**kw)
    return wraper

@ log                              #@在交互模式下不行要执行文件才可以
def now():
    print('2020-4-1- 17:11')

now()
print('func name is ',now.__name__)
# func name is  wraper