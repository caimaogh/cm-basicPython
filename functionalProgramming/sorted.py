#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序;
L1 = [22, -45, 99, -120, 0.3]
print(sorted(L1))
# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
print(sorted(L1, key = abs))

L2 = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(L2))
print(sorted(L2, key = str.lower))
# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(L2, key = str.lower, reverse = True))


L3 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(L3[0])

def by_name(name):
    return name[0]


def by_score(score):
    return score[1]

print(sorted(L3, key = by_name))
print(sorted(L3, key = by_score))
