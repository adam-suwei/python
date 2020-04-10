


# bytes 只接受ascII
 #Python对bytes类型的数据用带b前缀的单引号或双引号表示：

qqq = b'abc' #qqq is bytes
print('qqq in bytes is:',qqq) # b'abc'

bts=b'a2c'
bts[0]
#97  #返回a的ascii

#----------------------------------------------------------------------------------#
#
#           encode() decode()  str与 bytes 转换
#
#----------------------------------------------------------------------------------#


#以Unicode表示的str通过encode()方法可以编码为指定的bytes
'ABC'.encode('ascii') #bytes的每个字符都只占用一个字节
'孙玉铭'.encode('gb2312') #6个长度 b'\xcb\xef\xd3\xf1\xc3\xfa'   \x** 表示

'孙玉铭'.encode('utf-8') #b'\xe5\xad\x99\xe7\x8e\x89\xe9\x93\xad'

'中文'.encode('ascii') #超过128 error

#要把bytes变为str，就需要用decode()方法

b'ABC'.decode('ascii')
b'ABC'.decode('utf-8')

b'\xe5\xad\x99'.decode('utf-8')#孙

b'\xe5\xad\x99\xff'.decode('utf-8',errors='ignore') #孙
b'\xe5\xad\x99\xff'.decode('utf-8')  #报错

b'\xad\x99\xe7'.decode('utf-8',errors='ignore') #乱写的 返回‘’
b'\xad\x99\xe7'.decode('utf-8') #报错

#----------------------------------------------------------------------------------#
#
#           len() 获得str byte长度
#
#----------------------------------------------------------------------------------#

#len() 可以得到str字符个数 和bytes字节个数
len('ABC') # 3
len('孙玉铭') #3 返回字符非字节
bytess = '孙玉铭'.encode('utf-8') #返回字节
len(bytess) #得到9 

bytess = '孙玉铭'.encode('gb2312')
len(bytess) # return 6

len(b'\xe5\xad\x99') #3

