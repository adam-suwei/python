int('123')
int(123)
int('')
int(True) #1
int(None) #error
int(ord('a'))
#97

float('12.5')
float(12.5)
float(12)

str(123)
str('123abc')
str({'a':1,'b':2})

b = range(10)
str(b)
type(b)

# >>> str(b)
# 'range(0, 10)'
# >>> type(b)
# <class 'range'>

# -----------------------------------------
# 0 空集合 None都是False
bool(0)
bool(1)
bool(None)
bool('a')
bool(b'a')
bool(set('abc'))
bool(set())
bool([])

# >>> bool(0)
# False
# >>> bool(1)
# True
# >>> bool(None)
# False
# >>> bool('a')
# True
# >>> bool(b'a')
# True
# >>> bool(set('abc'))
# True
# >>> bool(set())
# False
# >>> bool([])
# False


#--------------------------------------
# 方法名作为变量引用
a = abs
a(-1)  #1

hex(9821111)
# 0x95dbb7

a = input('请输入您要转换的的十进制：')
b = int(a)
print('您输入的十进制%s 转换为十六进制是：%s' % (a,hex(b)))