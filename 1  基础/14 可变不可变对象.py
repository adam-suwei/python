
#-----------------------------------------
#不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的

# Python中不可变对象：int, float, str, tuple, bool
# Python中可变对象: list, dict, set
#-----------------------------------------


# 不可变对象：
# 　　a = 5 PK a= 4: 在5的内存地址和4的内存地址是不同的

# 可变对象：
# 　　list = [1, 2, 3, 4] PK list.append(5, 6): 这中的list的内存地址是相同的




# a.replace 仅仅是拿出一份复制品
a = 'abc'
a.replace('a', 'A')  # 等于b = a.replace('a', 'A')
#'Abc'
a
#'abc'

#不可变
i = 8
i-8
#0
i 
#8

# list已经变化了
l = [1,2,3,4]
l.sort()
l
#[1, 2, 3, 4]  l的数据位置变化了




# * 放在dict 和 set中的元组或者列表中的每一个对象都是用作为key的。如（1,2,3）可以，但（1，[2,3]）则不可以【2,3】是可变的
