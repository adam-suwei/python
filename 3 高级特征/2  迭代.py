
#-------------------------------------------------------
# 遍历顺序执行名为，迭代
# for 只关心迭代器 iterable 不关心其types
from typing import Iterable
# typing常用的类型：

# int,long,float: 整型,长整形,浮点型;
# bool,str: 布尔型，字符串类型；
# List, Tuple, Dict, Set:列表，元组，字典, 集合;
# Iterable,Iterator:可迭代类型，迭代器类型；
# Generator：生成器类型；
isinstance('abcdefg',Iterable)
#True
isinstance(1234,Iterable)
#False


#bytes------------------------
b = b'abcde'
b[1]
#98

for i in b:
    print(i)
# 97
# 98
# 99
# 100
# 101


# str------------------------
s = 'abcde'
for i in s:
    print(i)
# a
# b
# c
# d
# e

# list------------------------
l = list(range(5))
for i in l:
    print(i)
# 0
# 1
# 2
# 3
# 4

# tuple------------------------
l = tuple(range(5))
for i in l:
    print(i)
# 0
# 1
# 2
# 3
# 4

# dict------------------------
d = {'a':1,'b':2,'c':3}
for i in d:  #=d.items()
    print(i)
# ('a', 1)
# ('b', 2)
# ('c', 3)

d = {'a':1,'b':2,'c':3}
for i in d.items():
    print(i)
# ('a', 1)
# ('b', 2)
# ('c', 3)


d = {'a':1,'b':2,'c':3}
for i in d.keys():
    print(i)
# a
# b
# c

d = {'a':1,'b':2,'c':3}
for i in d.values():
    print(i)
# 1
# 2
# 3

# set------------------------

set = set('1234567')
for i in set:
    print(i)
# 1
# 6
# 7
# 4
# 2
# 3
# 5

#-----------------------------
# enumerate()

# str
x ='123'
for i,v in enumerate(x):
    print(i,'-',v)
# 0 - 1
# 1 - 2
# 2 - 3

# bytes
x =b'123'
for i,v in enumerate(x):
    print(i,'-',v)
# 0 - 49
# 1 - 50
# 2 - 51

# list
x =[1,2,3]
for i,v in enumerate(x):
    print(i,'-',v)
# 0 - 1
# 1 - 2
# 2 - 3

# tuple
x =(1,2,3)
for i,v in enumerate(x):
    print(i,'-',v)
# 0 - 1
# 1 - 2
# 2 - 3

# dict
x ={'a':1,'b':2,'c':3}
for i,v in enumerate(x):  #默认取key  so as  x.value()s, x.items()
    print(i,'-',v)
# 0 - a
# 1 - b
# 2 - c

# set
x =[1,2,3]
for i,v in enumerate(x):
    print(i,'-',v)
# 0 - 1
# 1 - 2
# 2 - 3

#-----------------------------
# i v 多值迭代

x = [[10,11],[20,21],[30,31]]
for i,v in x:
    print(i,'-',v)
# 10 - 11
# 20 - 21
# 30 - 31

#------------------------------
# 作业A

from typing import Iterable

def findMinAndMax(l):
    if not isinstance(l,list):
        return '请输入可迭代数据类型'
    if len(l)==0:
        return None,None
    m =l[0]
    n =l[0]
    for i in l:
        if i >m:
            m = i
        if i < n:
            n = i


    print('n = ',n ,' m = ',m)
    
    return n,m

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')


    from typing import Iterable

#------------------------------
# 作业A1
def findMinAndMaxs(l):
    if not isinstance(l,list):
        return '请输入可迭代数据类型'
    if len(x)==0:
        return None,None

    x.sort()
    print('x = ',x)
    
    return x[0],x[-1]

# 测试
if findMinAndMaxs([]) != (None, None):
    print('测试失败!')
elif findMinAndMaxs([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMaxs([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMaxs([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')