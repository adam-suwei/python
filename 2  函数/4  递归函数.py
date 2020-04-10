
# n! = (n-1)!*n

def fact(num):
    if num ==1:
        return 1

    print('%d!*%d' % (num-1,num))
    y = fact(num-1)*num
    print('%d!*%d=%d' % (num-1,num,y))
    return y

fact(5)
# 4!*5  FIFO stack 堆栈
#   3!*4
#       2!*3
#           1!*2
#           1!*2=2
#       2!*3=6
#   3!*4=24
# 4!*5=120
# 120

#-----------------------------------------
# 递归栈溢出
fact(1000)
#...
#5!*6 
# 超出python对象最大调用深度1000-5

#-----------------------------------------
# 尾递归优化， Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。
def fact1(n):
    return fact_inter(n,1)

def fact_inter(num,reslt):
    if num ==1:
        return reslt
    print('%d!*%d' % (num-1,num))
    y = fact_inter(num-1,num*reslt)
    print('%d!*%d=%d' % (num-1,num,y))
    return y

#fact1(5)
# 4!*5
# 3!*4
# 2!*3
# 1!*2
# 1!*2=120
# 2!*3=120
# 3!*4=120
# 4!*5=120
# 120
fact1(1000)
#...
#6!*7 
# 超出python对象最大调用深度1000-6