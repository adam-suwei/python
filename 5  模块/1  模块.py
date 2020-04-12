# 在Python中，一个.py文件就称之为一个模块（Module）
 

# Python又引入了按目录来组织模块的方法，称为包（Package）。
# mycompany
#  ├──── web
#  │      │
#  │      ├─ utils.py
#  │      └─ abc.py
#  │
#  └─ utils.py
# 文件www.py的模块名就是mycompany.web.abc，两个文件utils.py的模块名分别是mycompany.utils和mycompany.web.utils
# 自己创建模块时要注意命名，不能和Python自带的模块名称冲突。例如，系统自带了sys模块，自己的模块就不可命名为sys.py
# mycompany.web也是一个模块，请指出该模块对应的.py文件。

# Python变量命名规范，不要使用中文、特殊字符；

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'adam.sun'

import sys

def test():
    # sys模块有一个argv变量，用list存储了命令行的所有参数。
    args=sys.argv
    if len(args) == 1:
        print('hello world 1 ,',args[0])
    elif len(args)==2:
        print(' hello,%s!' % args[1])
    else:
        print('Too many args!')

print(__name__ )
print(__author__)
# __main__
# adam.sun

# 在命令行运行hello文件，__name__ ==__main__,如果是代码调用就不是了
if __name__ =='__main__':
    test()

# python a.py
# hello world 1 , a.py

# python a.py 朵朵 
# __main__
# adam.sun
#  hello,朵朵!

# PS D:\python\python> python
# >>> import a
# >>> a.test()
# hello world 1 



# 函数变量定义：
# public: 公开的函数和变量名（public），可以被直接引用，比如：abc，x123，PI等；
# private：类似_xxx和__xxx这样的函数或变量就是非公开的（），不应该被直接引用，比如_abc，__abc等；
# 特殊变量：类似__xxx__这样的变量是特殊用途变量，如__author__，__name__,文档注释也可以用特殊变量__doc__访问，自己不要用__XXX__定义变量名


# 代码封装和抽象的方法
def _private_1(name):
    return '_private_1 ,%s' % name

def _private_2(name):
    return '_private_2 ,%s' % name

def greeting(name):
    if len(name) >3:
        return _private_1(name)
    else:
        return _private_2(name)

# >>> import a

# >>> a.greeting('adam')  
# '_private_1 ,adam'
# >>> a.greeting('aha')  
# '_private_2 ,aha'

