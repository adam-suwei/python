# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。

#赋值
classmete =  ['adam','peter','joy','judy']
classmete 

l = list('01234567')
l = list(range(8)) # 不包括8

#获得长度
len(classmete)  #4

#按索引取值
classmete[0]
classmete[1]
classmete[2]
classmete[3]
classmete[4] #oor

# 取得最后一个元素
classmete =  ['adam','peter','joy','judy']
l1 = len(classmete)
classmete [l1-1]
classmete[-1]
classmete[-2] #可以-2 ^_^ 


#倒数是可以从1开始数到len的，倒数时下标不用减去1

classmete =  ['adam','peter','joy','judy']
l1 = len(classmete)
l2=5
if l1<l2:   # 不用减去1
    'oor' 
else:
    classmete[-3] 


#list是一个可变的有序表，所以，可以往list中追加元素到末尾：
boys =  ['adam','peter','joy','judy']
boys.append('test')
boys
boys[len(boys):]

#extend 添加list
boys =  ['adam','peter','joy','judy']
boys.extend(['adam','b'])
boys
#   ['adam', 'peter', 'joy', 'judy', 'adam', 'b']

#清空list
boys =  ['adam','peter','joy','judy']
boys
boys.clear()
boys #[]

# 插入中间插入
boys =  ['1','2','3','4'] #一个list里面可以各种类型
boys.insert(1,99)  #['1', 99, '2', '3', '4']
boys

# 可以倒数着插入
boys.insert(-1,'b')  # ['1', '2', '3', 'b', '4']
boys

#要删除list末尾的元素，用pop()方法： pop()=pop(-1)
boys =  ['1','2','3','4'] 
boys.pop() #['1', '2', '3']
boys

boys =  ['1','2','3','4'] 
boys.pop(0)  #['2', '3','4']
boys
boys.pop(4)  # Error oor
boys

boys =  ['1','2','3','4'] 
boys.pop(-2)  #可以倒数删除   #['1', '2', '4']
boys

# remove 删除字符，pop删除位置
boys =  ['1a','2','1a','4'] 
boys.remove('1a') #['2', '1a', '4']
boys

boys.remove('a') # Error not in list
boys



#替换
boys =  ['1','2','3','4'] 
boys[-2] = '3a'
boys                      #['1', '2', '3a', '4']

boys =  ['1','2','3','4'] 
boys[3] = '4a'
boys                      #['1', '2', '3', '4a']


#多维数组

multA =['a',['b1','b2',['b3a','b3b']],'c']
multA[0]       #'a'
multA[1]       #['b1', 'b2']
multA[1][1]

listA = multA[1] 
listA[1]  #'b2'

strB = multA[1][2][0]
strB     #'b3a'

#index 计算某元素出现第一个位置
boys =  ['1a','2','1a','4'] 
i=boys.index('1a')
i                     #0

#index 从片段中找出现位置
boys =  ['1','2','1','4'] 
i= boys.index('1',1,3) # 2 1 4中找
i                      #return 2   返回1 2 1 4中的位置

#count 计算某元素出现的次数
boys =  ['1a','2','1a','4'] 
i=boys.count('1a')
i                            #return 2


#sort 排序 sort() 没有返回值，修改了原list
boys =  ['a','b','d','c'] 
boys.sort()
boys                     #['a', 'b', 'c', 'd']

boys =  ['1','a','2','b'] 
boys.sort()
boys                     #['1', '2', 'a', 'b']
boys[2]                  # a 而不是2 说明list数据位置变化了


boys =  [1,'a',2,'b'] 
boys.sort()
boys                     #不支持多类型之间排序


#reverse() 反转列表中的元素 修改原数组
boys =  ['a','b','c','d'] 
boys.reverse()
boys                     #['d', 'c', 'b', 'a']

boys =  ['a','b','c','d'] 
boyss=boys[::-1]  #反转取值
boys              #['a', 'b', 'c', 'd']
boyss             #['d', 'c', 'b', 'a']


#copy 直接复制 = ：

boys =  ['a','b','c','d'] 
boya=boys.copy()
boyss=boys[:]
boya
boyss

#pop 作为堆栈 有返回值
boys =  ['a','b','c','d'] 
str = boys.pop()
boys
str

# 使用deque做序列，list从尾部效率高，从头部pop()效率很低(因为所有item位置都要移动)
from collections import deque
boys =  ['a','b','c','d'] 
deque = deque(boys)
deque.popleft()
boys            #boys没有变化 ['a','b','c','d'] 
deque           #deque [b','c','d'] 
boys

# 多维赋值
boys=[1,2]
boys[1]=['a','b']
boys

boys=[1,['a','b']]
boys[1].append('c')
boys

boys = [1,['a','b']]
boys[1][1]

boys[1][1]=[31,42] 
boys  #[1, ['a', [31, 42]]]


boys=[1,2]
boys.append(['a','b','c'])
boys

# list()方法可以把序列转换成list 列表才能打印出来
list(range(10))
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 遍历list
l = [1,2,3]
for i in l:
    print(i,type(i))


#list赋值给三个变量
a,b,c =[1,2,3]
a
b
c
# 1
# 2
# 3











