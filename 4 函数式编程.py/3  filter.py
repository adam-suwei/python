# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。


# 过滤掉所有奇数
def isodd(x):
    return x%2==0

list(filter(isodd,[0,1,2,3,4,5,6,7,8,9]))  #筛选
# [0, 2, 4, 6, 8]

def isEmpty(x):
    return x !=' '

# 去除所有空格
list(filter(isEmpty,' 1 2 3 4 5 6 7 '))
# ['1', '2', '3', '4', '5', '6', '7']

'1 '.strip()

def not_empty(s):
    print('s==',s)
    print('s and s.strip()==',s and s.strip())
    print('bool  is：',bool(s and s.strip()))

    return s and s.strip()

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))

# 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，
# 所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list


def primes():
    print('执不执行！1')
    yield 2
    print('执不执行！2')

    it = iter(range(10,20)) # 初始序列
    print('执不执行！3')

    while True:
        print('执不执行！4')
        n = next(it) # 返回序列的第一个数
        print('执不执行！5')

        yield n
        print('执不执行！6')

        it = filter(lambda x: x%n >0, it) # 构造新序列
        print('执不执行！7')

 # 执不执行！1
# 2
# 执不执行！2
# 执不执行！3
# 执不执行！4
# 执不执行！5
# 10
# 执不执行！6
# 执不执行！7
# 执不执行！4
# 执不执行！5
# 11
# 执不执行！6
# 执不执行！7
# 执不执行！4
# 执不执行！5
# 12
# 执不执行！6
# 执不执行！7
# 执不执行！4
# 执不执行！5
# 13
# 执不执行！6
# 执不执行！7
# 执不执行！4
# 执不执行！5

for n in primes():
    if n < 100:
        print(n)
    else:
        break


def is_palindrome(n):
    if not isinstance(n,int) or n< 0 :
        return False
    
    if n <10:
        return True

    if str(n) == str(n)[::-1]:
        return True

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')





