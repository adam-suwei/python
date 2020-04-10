# dict 就是java中的map


#
# 构造推导式 

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
a == b == c == d == e   #True

d = {x: x**2 for x in (2, 4, 6)}
d   #{2: 4, 4: 16, 6: 36}

#看看主类
d = {'a':1,'b':2,'3':3}

type(d) #<class 'dict'>
type(d.keys())  #<class 'dict_keys'>
type(d.values())    #<class 'dict_values'>
type(iter(d))   #<class 'dict_keyiterator'>



#dict() 仅仅使用与 Key 是字符串时 
d = dict(a=1,b=2,c=3)   #，1 = 1 报错
d   #{'a': 1, 'b': 2, 'c': 3}  1 =1 报错

d = dict(sape=4139, guido=4127, jack=4098)
d

#取值
d = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
e = d['a']
# e  1

d = {'a':1,'b':2}
e = d.get('a')
e #1

#取不到 打印None
d = {'a':1,'b':2}
e =d.get('e')
print('==',d.get('e')) # == None  Python的交互环境不显示结果


# #has_key() key里面是否有值
# d = {'a':1,'b':2}
# print('?',d.has_key('1'))

# copy() 值复制，各玩各的
d = {'a':1,'b':2,'c':3}
d1 =d.copy()
d1
d1['a'] =11
d['a'] = 10
d
d1
# >>> d
# {'a': 10, 'b': 2, 'c': 3}
# >>> d1
# {'a': 11, 'b': 2, 'c': 3}

# fromKeys() 把老dirt中的key拿来，values不要
d = {'a':1,'b':2,'c':3}
c = c.fromkeys(d)
c   #{'a': None, 'b': None, 'c': None}


# iter(d) = iter(d.keys())
d = {'a':1,'b':2,'c':3}
iter(d) # is object at  0x0000000001E19E00>

for i in iter(d):
    print(i)
# a
# b
# c

for i in iter(d.values()):
    print(i)
# 1
# 2
# 3


# reversed(d) == reversed(d.keys())
d = {'a':1,'b':2,'c':3}

for i in reversed(d.keys()):
    print(i)
# c
# b
# a

#指定找不到Key时返回 ^_^
d = {'a':1,'b':2}
e = d.get('e','^_^')
e #'^_^'

# setdefault()指定找不到时返回默认值
d = {'a':1,'b':2}
d.setdefault('black',0) 
d   #{'a': 1, 'b': 1, 'black': 0}

d = {'a':1,'b':2}
len(d)          # 2
len(d.items())  # 2
len(d.keys())   # 2
len(d.values()) # 2




#修改
d['a'] = 'a1'
# d {'a': 'a1', 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

#重复的后者覆盖前者
a ='a'
d = {'a':1,a:2,'c':3,'d':4,'e':5,a:6}
d  #{'a': 6, 'c': 3, 'd': 4, 'e': 5}

# keys() values()方法 items()方法 d.这三个方法都是建立新对象，两次同样的keys() 对象地址不同 == 返回False
d = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6}
print('d.keys() = ',d.keys())     #dict_keys(['a', 'b', 'c', 'd', 'e', 'f'])
print('d.values() = ',d.values()) #dict_values([1, 2, 3, 4, 5, 6])
print('d.items() = ',d.items())   #dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6)])

# in 判断是否存在key中
d = {'a':1,'b':2,}
bl = 'a' in d
print('a in d ?',bl)  # True

bl = 'a' not in d
print('a not in d ?',bl)  # True

k = 'a'  in d.keys()
print('a  in d.keys() ?',k)  # True

v = 1 in d.values()
print(' 1 in d.values()?',v) # True


# 删除key
d = {'a':1,'b':2}
d.pop('a')
d  #{'b': 2}

d = {'a':1,'b':2}
del d['a']
d  #{'b': 2}

d.clear()
d   #{}

del d
d   # name 'd' is not defined

#删除最后一对item
d = {'a':1,'b':2}
d.popitem()
d



# 和list比较，dict有以下几个特点：

# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多 【牺牲存储求速度】

# dict的key必须是不可变对象  字符串、整数 tuble等


d = {['a','b']:12,'c':3}    # err key不支持list 不允许设置

d = {('a','b','c'):123,'d':4}   #{('a', 'b', 'c'): 123, 'd': 4} 支持元组  tuple
d

d = {'a':1,'b':2}
key = [1,2,3,]   
d[key]      #不允许调用


#update() 取合集，相同key的覆盖
d1 = {'a':1,'b':2}
d2 = {'a1':1,'b':3}
d1.update(d2) #

d1  #{'a': 1, 'b': 3, 'a1': 1}

# 遍历 items()
d = {'a':1,'b':2,'c':3}
for k,v in d.items():
    print('Key:%s is %s' %(k,v) )
# Key:a is 1
# Key:b is 2
# Key:c is 3

# 遍历 keys()
d = {'a':1,'b':2,'c':3}
for k in  d.keys():
    print('Key : %s ' %(k) )
# Key : a
# Key : b
# Key : c


# 遍历 values()
d = {'a':1,'b':2,'c':3}
for v in  d.values():
    print('Value : %s ' %(v) )
# Value : 1
# Value : 2
# Value : 3   

# enumerate() 获取位置
d = {'a':1,'b':2,'3':3}
for i,v in enumerate(d.values()):
    print(' pose %d is %s' %(i,v))
#  pose 0 is 1
#  pose 1 is 2
#  pose 2 is 3


d = {'a':1,'b':2,'3':3}
for i,v in enumerate(d.items()):
    print(' pose %d is %s' %(i,v))
#  pose 0 is ('a', 1)
#  pose 1 is ('b', 2)
#  pose 2 is ('3', 3)

#list()
d = {'a':1,'b':2,'3':3}
l = list(d.items())
l   #[('a', 1), ('b', 2), ('3', 3)]




