# sorted(iterable, key=None, reverse=False)  

sorted([36, 5, -12, 9, -21])
# [-21, -12, 5, 9, 36]

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序

#按照绝对值排序
sorted([36,5,-12,9,-21],key=abs)
# [5, 9, -12, -21, 36]

sorted(['bob','about','Zoo','Credit'])
# ['Credit', 'Zoo', 'about', 'bob']

#按照小写排序
sorted(['bob','about','Zoo','Credit'],key=str.lower)  #lower不需要括弧
# ['about', 'bob', 'Credit', 'Zoo']

#先进行key的排序，之后将这个顺序翻转，不是把每个单词中的字母翻转
sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse = True)
# ['Zoo', 'Credit', 'bob', 'about']


#--------------------------------------------------------------
L = [('bob',75),('adam',92),('Bart',66),('Lisa',88)]

L2 = sorted(L,key=lambda x: x[1])
L2
