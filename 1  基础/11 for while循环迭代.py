
# for  in ：

names = ['a','b','c']

for name in names:
    print('你的同学有：',name)

# 你的同学有： a
# 你的同学有： b
# 你的同学有： c

y = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    y = y + x
print('sum 1~10 is',y)


y = 0
for x in range(10):
    y = y + x
print('sum 1~10 is',y)

# 
y=int(input('输入从多少开始加'))
y1=int(input('加到多少'))
z = 0
for x in range(y,y1+1):
    z = z + x
print('sum %d ~ %d is %d' %(y,y1,z))





# for  in  if  else  必须有break 否则else一定执行，else实际上是和if配套，但是缩进很奇怪
for i in range(10):
    print('i = ',i)
    if i == 12:
        print( 'found it! i = %s' % i)
        break
else:
    print('not found it ...')


# while

st = int(input('请输入开始计算的数字：'))
end = int(input('请输入计算到那个数字：'))
sum = 0
a = st

#倒着数
if end < st:
    b = a
    a = end
    end = b

while a <= end:
    sum = sum+ a
    a=a+1

print(' 从%d到%d计算结果为：%d' %(st,end,sum))