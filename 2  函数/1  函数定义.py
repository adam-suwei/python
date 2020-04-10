#----------------------------------------
#  获得函数说明信息 仅于交互模式

help(abs)

# >>> help(abs)
# Help on built-in function abs in module builtins:

# abs(x, /)
#     Return the absolute value of the argument.


#----------------------------------------
#  输入错误的参数个数和错误的类型

abs(-9)
abs(9)
abs(0.8)
abs(-0.8)
abs('a')
abs(1,1)

# >>> abs(-9)
# 9
# >>> abs(9)
# 9
# >>> abs(0.8)
# 0.8
# >>> abs(-0.8)
# 0.8
# >>> abs('a')
#TypeError: bad operand type for abs(): 'str'
# >>> abs(1,1)
# TypeError: abs() takes exactly one argument (2 given)


#----------------------------------------
#  可变长度输入参数

max(1,2,3,4,5,6,7)
max(range(100))
max('b','a')

# >>> max(1,2,3,4,5,6,7)
# 7
# >>> max(range(100))  # 0 ~ 99
# 99
# >>> max('b','a')
# 'b'

#----------------------------------------
#  函数定义  def ： 要记住


def sabs(x):
    if not isinstance(x,(int,float)):
        raise TypeError(' bad input arg ',type(x),' is not int or float! ')
        
    if x>=0:
        return x
    else:
        return -x

#------------------------
# 引入文件导入方法
# from a import sabs
# sabs(-99.9)
# 99.9


#-----------------------------------------------
#多个输出参数实际是tuple

import math

def move(x,y,step,angle=0):
    nx = x+ step*math.cos(angle)
    ny = y + step*math.sin(angle)  
    return nx,ny

# from a import move
x1 =move(100,100,50,math.pi/6) # 2pi = 360 pi =180 pi/6 = 30
print(x1)
# (143.30127018922195, 125.0)

x , y=move(100,100,50,math.pi/6) # 2pi = 360 pi =180 pi/6 = 30
print(x,y)
# 143.30127018922195 125.0

#--------------------------------------------------
# 作业  ax*x + bx + c = 0

import math
#math.sqrt(9) # 3.0 求根

def quadratic(a,b,c):

    if (not isinstance(a,(int ,float)) ) or (not isinstance(c,(int ,float)) )  or (not isinstance(c,(int ,float)) ) :
        raise TypeError('bad arg types')

    if a == 0:
        if b == 0 and  c != 0:
            return(' %s == 0 不成立 ' % c)
        elif b ==0 and c == 0:
            return (' 原则上你可以录入任何x都可以满足a b c =0的解释')
        x = -c/b
        print(' a == 0 x =',x)
        return x

    m = b*b - 4*a*c
    if m < 0:
        return('此方程无解')

    elif m == 0:
        x = -b / 2*a
        print('此方程有且只有一个解：x=%.1f'%x)
        return x

    else:
        x1 = (-b - math.sqrt(m)/ (2*a))
        x2 = (-b + math.sqrt(m)/ (2*a))
        print('此方程式有两个解，x1=%.1f,x2=%.1f'%(x1,x2))
        return x1 ,x2

# from  a import quadratic 
print(quadratic(1,0,-36))
