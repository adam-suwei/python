
#---------------------------------------------------
#
#  set 是可变数据，但是他的内容必须是不可变数据 无序不重复,重复赋值，覆盖前者
#      所有计算运算返回新集合
#---------------------------------------------------


#---------------------------------------
#构造函数 set(list)
s = set([1, 2, 3, 3])
s
#{1, 2, 3}


a = set('abcdabc')
a
# {'a', 'd', 'b', 'c'}

a = set(range(10))
a
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}


s.add(4)
s
#{1, 2, 3,4}

#------------------------------------
# 删除
s = set([1, 2, 3, 4])

s.remove(4)
s
#{1, 2, 3}  
s.remove(4)
s
#KeyError: 4 不存在就报错

s.discard(4)   #放弃
s
# {1, 2, 3} 不存在不报错
s = set('abcde')
s
s.pop() 
#'d'  随机移除一个 有返回时
s
# {'a', 'e', 'b', 'c'}
s.pop() 
#'a'  随机移除一个 有返回时
s
# {'e', 'b', 'c'} 


#------------------------------------ 
# update修改了源集合，union 和 | 新建了一个集合视图
s = set([1, 2, 3])
t1 = set([2, 3, 4, 5])

s.union(t1)
s
# {1, 2, 3}

s | t1
s
# {1, 2, 3}

s.update(t1)
s
#   {1, 2, 3, 4, 5} s被改变了

# set计算



s1 = set([1,2,3])
type(s1)
#<class 'set'>

str(s1)
#'{1, 2, 3}'

len(s1)
#3

# in 操作
s1 = set([1,2,3])
2 in s1
#   True



#------------------------------------ 
# == 计算是对集合内部的比较不是对对象地址的比较

a = set('abc')
b = set('acb')

a == b
#  True


a = set('abcd')
b = set('cdef')
c = set('123')
d = set('cd')
#---------------------------------------
# 判断不相交集合

a.isdisjoint(c)
#   True a和b不相交


#---------------------------------------
# 判断子集 difference = <= 运算符

d.difference(a)
# True d是a的子集

d <= a
# True 是子集
b<=a
#   False 相交但是非子集

# 真子集
d <= a
# True 是真子集

#---------------------------------------
# 判断父集合，超集合 issuperset = >= 运算符  

a.issuperset(d)
# True a是d的超集合

a >= d
# True a是d的超集合

a >d
# True a是d的真超集合


#------------------------------------
# 合并操作  union = | 运算符  返回新视图

a = set('abcd')
b = set('cdef')
c = set('123')


a.union(b).union(c)  #返回合并新视图，原集合不变
a | b | c
a
c

# {'e', '2', '3', 'a', '1', 'd', 'c', 'b', 'f'}
# {'e', '2', '3', 'a', '1', 'd', 'c', 'b', 'f'}

# {'e', '2', '3', 'a', '1', 'd', 'c', 'b', 'f'}
# {'d', 'c', 'b', 'a'}
# {'1', '3', '2'}

a | b | c  #返回合并新视图，原集合不变
a
c

# {'e', '2', '3', 'a', '1', 'd', 'c', 'b', 'f'}
# {'d', 'c', 'b', 'a'}
# {'1', '3', '2'}

#------------------------------------
# 取交集操作  intersection = & 运算符  返回新视图

a = set('abcd')
b = set('cdef')

a.intersection(b).intersection(d)
a & b & d
#{'c', 'd'}

a.intersection(b).intersection(c)
#set() 返回空set

# 将交集结果重新设置原视图
a.intersection_update(b)
a
# {'d', 'c'}




#------------------------------------
# 取不同数据操作   difference = - 运算符  返回新视图

a = set('abcd')
b = set('cdef')
c = set('bc')


a.difference(b) #在a中不在b中的
a - b
#{'b', 'a'}

a.difference(b).difference(c)
a-b-c
# {'a'}
b.difference(a) #在b中不在a中的
b - a
# {'e', 'f'}

a.difference_update(b)
a
# {'a', 'b'} a已经变化

#------------------------------------ 
# 取互不相同的  symmetric_difference = ^  运算符  返回新视图
a = set('1b')
b = set('bc2')
c = set('c3')

a.symmetric_difference(b)
a ^ b
# {'f', 'b', 'e', 'a'}

a.symmetric_difference(b).symmetric_difference(c)
a ^ b ^ c
# {'2', '1', '3'}












































