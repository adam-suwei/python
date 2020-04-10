#注意冒号和缩进
age = 14
if age>=18:
    print(' your age more than 18 ',age)
else:
    print('your age is less than 18 ',age)   

# elif的嵌套
age = 8

if age >= 18:
    print('more than 18 : ', age)
elif age >= 16:
    print('more than 16 : ', age)
    print('more than 16 : ', age)
elif age >= 12:
    print('go home boy! : ', age)
else:
    print('haha')



# 输入类型转换 int() 简单的字符转数字，input输入的都是字符串
s = input(' input your age:')
print( '---:',s)
t = int(s)

if t < 2000:
    print('00 前')
elif t<3000:
    print('00 后')
else:
    print('你还没出生那')


# 作业
height = input('请输入您的身高单位米:')
weight = input('请输入您的体重单位公斤：')

bmi = float(weight)/(float(height)**2)

if bmi< 18.5:
    print('您的BMI指数为：[%.02f],体重[过轻]！' % bmi)
elif bmi <=25:
    print('您的BMI指数为：[%.02f],体重[正常]！' % bmi)
elif bmi <=28:
    print('您的BMI指数为：[%.02f],体重[过重]！' % bmi)
elif bmi <=32:
    print('您的BMI指数为：[%.02f],体重[肥胖]！' % bmi)
else:
    print('您的BMI指数为：[%.02f],体重[严重肥胖]！' % bmi)


