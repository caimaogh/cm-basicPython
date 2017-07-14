#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python的for循环抽象程度要高于Java的for循环，因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上
# dict迭代,dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样
d = {'1': 100, '2': 200, '3': 300, '4': 400, '5': 500}
for key in d:
    print(key)
#    print(d[key])
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()
for value in d.values():
    print(value)
# 如果要同时迭代key和value，可以用for k, v in d.items()
for k, v in d.items():
    print(k)
    print(v)

# 字符串也是可迭代对象，因此，也可以作用于for循环
S = '字符串也可以看作是一种list'
for ch in S:
    print(ch)

# 通过collections模块的Iterable类型判断一个对象是可迭代对象

from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance((1, 2, 3), Iterable))
print(isinstance({'1': 1, '2': 2}, Iterable))
print(isinstance(set([0, 1, 3,5, 7, 9]), Iterable))
print(isinstance(12345, Iterable))

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)