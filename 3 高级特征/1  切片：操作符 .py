#--------------------------------------------
#Python中，代码不是越多越好，而是越少越好。代码不是越复杂越好，而是越简单越好。
# 1行代码能实现的功能，决不写5行代码。请始终牢记，代码越少，开发效率越高。
# : 操作符是复制新视图

l = list('01234567')
l = list(range(8))  # 从0到7 共8
print(l[0:10])
print(l[:7])
print(l[1:3])
#[0, 1, 2]
#[0, 1, 2]
#[1, 2]

#--------------------------------------
#负数坐标向后取

l = list('01234567')
l[-3:] #从-3,-2,-1正向数
# ['5', '6', '7']

l1 = list(range(100)) #0到99 共100
l1

l1[:10]  #前十个
l1[-10:] #后十个
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

l1 = list('01234567')
l1[1:-2]
#['1', '2', '3', '4', '5']

#--------------------------------------
#跳着取

l1 = list(range(100)) #0到99 共100

l1[:10:2]
#[0, 2, 4, 6, 8]

l1[::5]
l1[0:100:5]
# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

l1[:] #取 复制出一个新list

#--------------------------------------
#倒着取
l1 = list(range(100)) #0到99 共100

l1[1::-1]
#[1, 0] 不填写就是到最左端

l1[10:1:-1]  #[1:10:-1]不可以  因为是向左数
#[10, 9, 8, 7, 6, 5, 4, 3, 2] vv

l1[-1:-10:-1]
#[99, 98, 97, 96, 95, 94, 93, 92, 91]  不包括-10 倒数从-1 无0



#--------------------------------------
# tuble 也可以切

[0,1,2,3,4,5][1:4]
#[1, 2, 3]
(0,1,2,3,4,5)[1:4]
#(1, 2, 3)

#--------------------------------------
# 字符串也可以切,python不提供截取字符串的函数3.8.2

'abcdefg'[1:4]  #此时视为bytes，结果仍为str
#'bcd'

'abc'[1]

#--------------------------------------
# bytes可以

b'abcd'[1]
#98    取下标时返回b的ASCII
b'abcd'[1:4]  
#b'bcd' 取范围时返回bytes

#--------------------------------------
#作业

def trim(astr,char=' ' ):
    if not isinstance(astr,str):
        return '请输入字符串'
    x=0      
    while x < len(astr):
        if astr[x] == char:
            x=x+1
        else:
            break
    print('x =',x)

    y=-1
    while y >= -len(astr): #倒着数
        if astr[y] == char:
            y =y-1
        else:
            break
    if  y != -1:
        y = y+1        #因为找到2个 y是-3，第三个倒数字符又是切片排除的，所以要+1
    else:
        y = len(astr)  #说明倒数没有空格，切片时后端不能是0 所以要去len

    print('y =',y)
    return astr[x:y]

print('[',trim('   ---'),']')
            

'aaaa123aaaa'[0:-1]

