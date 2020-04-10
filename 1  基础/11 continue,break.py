for n in range(2,10):
    for x in range(2,n):
        if n%x ==0:
            print('%d eques %d * %d' %(n,x,n//x))
            break   # 6 可以被2和3整除 这里找到一个就退出整个for循环结束。
    else:
        print('%d is a 素数！'% n)

# 2 is a 素数！
# 3 is a 素数！
# 4 eques 2 * 2
# 5 is a 素数！
# 6 eques 2 * 3
# 7 is a 素数！
# 8 eques 2 * 4
# 9 eques 3 * 3       

for num in range(2,10):
    if num % 2 == 0 :
        print(num,'是偶数')
        continue            #仅仅退出当前循环，继续下个N+1
    print('现在循环到了数字',num)


# and or not 运算符
if (True) and not(False):  #& = and | = or
    print('yes')
else:
    print('no')

