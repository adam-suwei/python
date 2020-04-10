#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Iterable

def findMinAndMax(l):
    if not isinstance(l,list):
        return '请输入可迭代数据类型'
    if len(l)==0:
        return None,None
    m =l[0]
    n =l[0]
    for i in l:
        if i >m:
            m = i
        if i < n:
            n = i


    print('n = ',n ,' m = ',m)
    
    return n,m

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')