# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

#map() 加工---------------------------------------
# Iterable-------->Iterator

def  f(x):
    return x*x

r = map(f,[1,2,3,4,5,6,7,8,9,10])
list(r)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#循环代码，是不能一眼看明白“把f(x)作用在list的每一个元素并把结果生成一个新的list”的。这就是python的高度抽象，不关注细节

# 只需要一行代码把所有数字转成字符
list(map(str,[1,2,3,4,5,6,7,8]))
# ['1', '2', '3', '4', '5', '6', '7', '8']



#reduce -------------------------------------------
# reduce把一个函数作用在一个序列上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)


from functools import reduce

def add(x,y):
    return x+y

reduce(add,[1,2,3,6,12,24])
# 48  = 
add(add(add(add(add(1,2),3),6),12),24)
# 48  = 

def conl(x,y):
    return x*10+y

reduce(conl,[1,2,3,4,5,6,7,8,9])
# 123456789

#-map负责清洗---reduce负责计算
reduce(conl,map(int,'123456789'))
# 123456789

# 使用lambda表达式
reduce(lambda x,y:x*10+y,map(int,'123456789'))
# 123456789

#----------------------------------------------------
# 作业A
def norm(name):
    return name[0].upper()+name[1:].lower()

L1 = ['adam', 'LISA', 'barT']
list(map(norm,L1))

#----------------------------------------------------
# 作业B

def prod(x,y):
    return x*y

reduce(prod,[1,2,2,4,16])
# 256

reduce(lambda x,y: x*y,map(int,'12345'))
# 120

#----------------------------------------------------
# 作业B'

def pro(l):
    return reduce(lambda x,y: x*y,l)

print('3 * 5 * 7 * 9 =', pro([3, 5, 7, 9]))
if pro([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

    
#----------------------------------------------------
# 作业c

def str2Float(s):
    i=s.count('.')
    if i==0:
        return reduce(lambda x,y: x*10+y,map(int,s))
    

    i = s.index('.')    
    s1=s[:i]
    s2=s[:-i-1:-1]   # '.'点不要了 ab.123-->321
    r1=reduce(lambda x,y: x*10+y,map(int,s1))   #((a*10+b)*10+c)*10+d
    r2=reduce(lambda x,y: x/10+y,map(int,s2))   #1+0.1*(2+0.1*3))   321-->1.23
    return r1+r2*0.1   #1.23--->0.123

print('str2float(\'123.456\') =', str2Float('123.456'))
if str2Float('123.456') == 123.456:
    print('测试成功!')
else:
    print('测试失败!')

