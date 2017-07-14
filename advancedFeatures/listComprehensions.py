#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python内置的非常简单却强大的可以用来创建list的生成式
L1 = list(range(1,11))
print(L1)

# 生成[1x1, 2x2, 3x3, ..., 10x10] 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环
L2 = [x * x for x in range(1, 11)]
print(L2)
# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
L3 = [x * x for x in range(1, 11) if x % 2 == 0]
print(L3)
L4 = [x * x for x in range(1, 11) if x % 2 == 1]
print(L4)

# 还可以使用两层循环，可以生成全排列
L4 = [m + n for m in 'ABC' for n in 'XYZ']
print(L4)

L5 = ['Select', 18, 'FROM', 'TabLe', None]
L6 = [s.lower() for s in L5 if isinstance(s, str)]
print(L6)