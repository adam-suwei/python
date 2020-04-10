# 元组：tuple。tuple和list非常类似，一旦赋值股允许改变
classmate = ('a','b','c')
classmate[1]
classmate.index('b')

#单值元组区别于和数字括弧
ta=(1) # int
tb=(1,) #tuple

#空的元组
tc=()
tc

#可变元组 tuple 仅对第一层地址管理，只管对象地址和数值管控，对象内部数值管不了
ta=('a','b',['1','2'])
ta[2][0]='sun'
ta[2][1]='yu'
ta            #('a', 'b', ['sun', 'yu'])

# ta[0]='a1' #编译时就报错了
# ta #Error 元组不支持修改内部项

# 除非定义的内部对象也是tuple
ta = ('a','b')
tb= ('1',ta)
tb

#tb[1][1] = 'x'  #编译时就报错了
#tb              #Error nsia

