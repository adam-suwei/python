

#变量转换

# Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符


chart = 'a'
print('ord(a)=',ord(chart))

asci = 0
print('ascii ',asci,' =',chr(asci))

# 中文字符超过了assii的范围 ord返回的是unicode的六位数字。
chart = '孙'
print(chart,' ascii = ',ord(chart))

asci = 90
print(asci,' is = ',chr(asci))

#十六进制 直接返回‘中文’


'\u4e2d\u6587' #返回 '中文'

