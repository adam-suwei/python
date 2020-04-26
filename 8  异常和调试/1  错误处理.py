#-----------------------------------------
# try 捕获

try:
    print('try...')
    r=10/2
    print('result:',r)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
except ValueError as e:
    print('ValueError:',e)
else:
    print('No Except! ')  #不出错才执行
finally:
    print('finally...')  #finally一定执行
print('End...')


# 所有的错误类型都继承自BaseException
# try...
# except division by zero
# finally...
# End...


#-----------------------------------------------------
#调用栈 logging.

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
# ERROR:root:division by zero
# Traceback (most recent call last):
#   File "<stdin>", line 3, in main
#   File "<stdin>", line 2, in bar
#   File "<stdin>", line 2, in foo
# ZeroDivisionError: division by zero

#-----------------------------------------------------
#抛出异常
class FooError(ValueError):
    pass

def foos(s):
    n = int(s)
    if n ==0:
        raise FooError('the Zero is devision ')
    return 10/n

foos(0)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 4, in foos
# __main__.FooError: the Zero is devision



# raise语句如果不带参数，就会把当前错误原样抛出
try:
    10/0
except ValueError as e:
    print('ValueError!')
    raise
# 在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
try:
    10/0
except ZeroDivisionError as e:
    raise ValueError('input error ')

# -------------------------------------------------
# 作业

from functools import reduce
import logging


def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def mains():
    try:
        r = calc('100 + 200 + 345')
        print('100 + 200 + 345 =', r)
        r = calc('99 + 88 + 7.6')
        print('99 + 88 + 7.6 =', r)
    except Exception as e:
        logging.exception(e)        

mains()
