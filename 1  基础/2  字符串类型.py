

# 字符数据类型 字符串
print("[ I '_' U ]")   
print('[ I \'_\' U ]') #error

print('[ I "_" U ]')  
print("[ I \"_\" U ]") #errpr

print('[ I \"_\' U ]')

print('I\'m learning \n\\python.\\\r\n\\')



 #r''表示''内部的字符串默认不转义

print(r'\\\r\n\\',128+2)

#'''...'''的用法直接所见即所得代码换行结果也换行  注意...是提示符，不是代码

print('''
第一行
第二行
第三行
''')

#r和'''嵌套 

print(r'''
第一行
\n
\\\\\n
''')

print('''
1
2
3
''',r'\\\n')

s1 = 'Hello,\"Adam\''
print('s1 = ',s1)

s3 = r'Hello,"\'\n'
print('s3 = ',s3)

s4 = r'''
Hello,
Lisa!
\n\r\t\\"'
'''
print('s4 = ',s4)

#---------------------------------------
# 字符串可以作为list直接使用,直接取下标或切片

'abcde'[1:3]
# 'bc'