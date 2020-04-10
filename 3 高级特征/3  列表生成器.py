#----------------------------------------------------


list(range(1,11))
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#[1x1, 2x2, 3x3, ..., 10x10]
l =[]
for i in range(1,11):
    l.append(i*i)
l
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# 使用;'['']'表示列表生成器
# for 循环生成器----------------------------
[x*x for x in range(1,11)]
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

[x*x+2*x+1 for x in [1,2,3,4,5,6,7]]
#[4, 9, 16, 25, 36, 49, 64]

#笛卡尔积
[m+n for m in 'abc' for n in 'ABC']
#['aA', 'aB', 'aC', 'bA', 'bB', 'bC', 'cA', 'cB', 'cC']

#二维笛卡尔积
[m+n for m in [['a11','a12'],['a21','a22']] for n in [['b11','b12'],['b21','b22']]]
#[['a11', 'a12', 'b11', 'b12'],
# ['a11', 'a12', 'b21', 'b22'], 
# ['a21', 'a22', 'b11', 'b12'], 
# ['a21', 'a22', 'b21', 'b22']]

#三个集合的笛卡尔积
[m+n+z for m in 'ab' for n in 'AB' for z in '12']
#['aA1', 'aA2', 'aB1', 'aB2', 'bA1', 'bA2', 'bB1', 'bB2']


# for + if 生成器---------------------------
[x*x for x in range(1,11) if x%3==0]  #这里if 不能有else
#[9, 36, 81]

# if + for if只是表达式不是条件--------------
[x*x if x==3 else -x for x in range(1,11) if x%3==0]  #这里if 必须要有else 是x的计算表达式不是过滤
# 如果x==3 表达式为x*x
# 如果x!=3 表达式为-x
# [9, -6, -9]

#-------------------------------------------
# 简化列出目录下所有文件
import os
[d for d in os.listdir('.')]  # '.'表示当前执行命令的路径，而非文件路径，方法列出路径下所有目录和文件

#-------------------------------------------
#for 循环可以两个变量

[str(x)+y for x ,y in enumerate(['a','b','c'])]
# ['0a', '1b', '2c']

#-------------------------------------------
# 两个循环 三个变量
d= {'1':'a','2':'b','3':'c'}
[k+v+z for k,v in d.items() for z in ['x','y','z']]
['1ax', '1ay', '1az', '2bx', '2by', '2bz', '3cx', '3cy', '3cz']

#---------------------------------------------
#生成中x可以使用函数

[s.lower() for s in ['A','B','C']]
#['a', 'b', 'c']

#---------------------------------------------
#作业
l = ['Hello', 'World', 18, 'Apple', None]
l2=[s.lower() for s in l if isinstance(s,str)]

print(l2)
if l2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

