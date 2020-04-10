

x =10
x=x+10
print('x = ',x)

# 变量交换是值传递 而不是地址传递
a = 'abc'
b = a
a = 'xyz'
print('abc = ',b)
print('xyz = ',a)

#/除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：
a = 10/3
print(a)

# //，%操作结果是整数
print(r'取商//\n:',10//3)
print(r'取余数\%',10%3)


f = 456.789

qqq = 123  #qqq is int [可变类型，类型可变]

qqq = b'abc' #qqq is bytes
print('qqq in bytes is:',qqq)

