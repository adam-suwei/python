# next() 返回迭代器的下一个项目。

# next() 函数要和生成迭代器的iter() 函数一起使用

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:        
        x = next(it)
        print(x)
    except StopIteration:
        print('--has no next()')
        # 遇到StopIteration就退出循环
        break

# 1
# 2
# 3
# 4
# 5
# --has no next()