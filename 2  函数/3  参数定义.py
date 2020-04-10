#---------------------------------------
# 默认参数，可变参数，关键字参数

#位置参数-----------------------------------------------------
def power(x):
    if  isinstance(x,(int,float)):
        return x**2
    else:
        return '请输入数字'

power(12)
#144


def powern(x,n):  # 乘幂运算
    if not isinstance(x,(int,float)) or not isinstance(n,int):
        return '请输入数字'
    
    return x**n

powern(5,2)
#25

#默认参数-----------------------------------------------------
#好处是能降低调用函数的难度
#默认参数必须在位置参数后面

def powerm(x,n=2):  # 乘幂运算  
    if not isinstance(x,(int,float)) or not isinstance(n,int):
        return '请输入数字'
    
    return x**n

powerm(5)
#25

# 默认参数的跳跃调用
def enroll(name,gender,age=16,city='nanjing'):
    print('nam   =',name)
    print('gender= ',gender)
    print('age   = ',age)
    print('city  = ',city)

enroll('朵朵','女',9)   #默认按顺序
enroll('朵朵','女',city='大华') #跳过顺序要指明参数

# 默认指向可变对象的悲哀
def add_end(l=[]): 
    l.append('End')
    return l

add_end()
add_end()
#['End']
#['End', 'End']  l只能理解为全局变量了

add_end(['a','b'])
#['a', 'b', 'End']

# 编程尽可量使用不可用变量
def add_enda(l=None):
    if l is None:
        l=[]
    l.append('End')
    return l

add_enda()
add_enda()



#--------------------------------------------------------------
# 可变参数 n是一个tuple 输入[0],taple[0]是list不是数字0

def calc(*n,power = 2):
    
    sum = 0
    for i in n:
        if not isinstance(i,(int,float)):
            raise TypeError(' 请输入数字！ ')
        sum=sum+i**power
    return sum

calc(1,2,3,2,power=1)
#8

# 把N个可变参数作为一个变量穿进去 
#*nums表示把nums这个list的所有元素作为可变参数传进去
nums = [1,2,3]
calc(*nums)
#14


#不允许多个可变参数

#--------------------------------------------------
#关键字参数 可以不输入 会把位参之外的放在dict中  

def person(name,age,**kw):
    print('name = ',name)
    print(' age = ',age)
    if 'hg' in kw:
        kw['hg'] ='071'
    print('  kw = ',kw)

person('adam',42,hg=170,wg=180)   #注意位参 此时关键字总不能有age
person('adam',hg=170,wg=180,age=42) #注意位参 此时不写位参age不报错，因为关键中有
person(name = 'a',age ='42',pw = 'password')
person(1,2) #关键字参数可以不写

# 使用** 带入实际参数
dic = {'hg':170,'wg':180}
person('adam',42,**dic)

# 使用** 带入实际参数
dic = {'name':'adam','age':42,'hg':170,'wg':180}
person(**dic)# 注意persion中对dic的修改不会改动dic 是值传递
#kw =  {'hg': '071', 'wg': 180}
dic
#{'name': 'adam', 'age': 42, 'hg': 170, 'wg': 180}

#--------------------------------------------------
# 【命名关键字】参数 对输入的关键字参数必须出现

def persona(name,age,*,hg,wg):
    print('name = ',name)
    print(' age = ',age)
    print('  wg = ',hg)
    print('  kw = ',wg)

persona('adam',42,hg =170,wg = 180) 
persona('adam',hg =170,wg = 180,age = 42) 
# name =  adam
#  age =  42
#   wg =  170
#   kw =  180

#persona('adam',42,hg =170) # 提示没有提供wg
#persona('adam',42,hg =170,wg = 180, kw ='benke') #报错，不能输入hg wg之外的

#*phone可变参数后面的只能是命名关键字,而且不用*
def personb(name,age,*phone,hg,wg):
    print('name = ',name)
    print(' age = ',age)
    print('phone = ',phone)
    print('  wg = ',hg)
    print('  kw = ',wg)

#personb('adam',42,139,180,170,180) * 不写key不行
personb('adam',42,139,180,hg=170,wg=180) 
# name =  adam
#  age =  42
#phone =  (139, 180)
#   wg =  170
#   kw =  180

# 有缺省值的命名关键字参数可以不输入
def personc(name,age,*phone,hg=170,wg):
    print('name = ',name)
    print(' age = ',age)
    print('phone = ',phone)
    print('  wg = ',hg)
    print('  kw = ',wg)

personc('adam',42,139,180,wg=180) 
# name =  adam
#  age =  42
#phone =  (139, 180)
#   wg =  170
#   kw =  180

#--------------------------------------------------
# 参数组合  参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

def f1(a,b=10,*num,hg,wg,**kw):
    print('  a = ',a)
    print('  b = ',b)
    print('num = ',num)
    print(' hg = ',hg)
    print(' wg = ',wg)
    print(' kw = ',kw)

f1('a1','b1',1,2,3,hg=170,wg=180,kw=18,dr='abc')
#   a =  a1
#   b =  b1
# num =  (1, 2, 3)
#  hg =  170
#  wg =  180
#  kw =  {'kw': 18, 'dr': 'abc'}
f1(hg=170,wg=180,kw=18,a='abc',num=[1,2,3])
#   a =  abc
#   b =  10
# num =  ()
#  hg =  170
#  wg =  180
#  kw =  {'kw': 18, 'num': (1, 2, 3)}

args =('1a','2b','3a','3b','3c')
kw ={'hg':170,'wg':180,'adr':'nanjing'}
f1(*args,**kw)
#   a =  1a
#   b =  2b
# num =  ('3a', '3b', '3c')
#  hg =  170
#  wg =  180
#  kw =  {'adr': 'nanjing'}

#-----------------------------------------------------
# 作业


def pdct(*num):

    sum = 1
    for i in num:
        if( not isinstance(i,(int,float))):
            return '——请输入数字！——'  
        sum =sum * i

    return sum

pdct(1,2,3,4)
#24
