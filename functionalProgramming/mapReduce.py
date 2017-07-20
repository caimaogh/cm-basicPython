#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python内建了map()和reduce()函数 map 映射 reduce 化简
# MapReduce is a programming model and an associated implementation for processing and generating large data sets.
# Users specify a map function that processes a key/value pair to generate a set of intermediate key/value pairs,
# and a reduce function that merges all intermediate values associated with the same intermediate key.

# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回


def f(x, y):
    return x * y

# map()传入的第一个参数是f，即函数对象本身。由于结果是一个Iterator(惰性序列)，因此通过list()函数让它把整个序列都计算出来并返回一个list
print(list(map(f, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10, 12])))
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# reduce() 函数接收两个参数，一个是函数，一个是 Iterable，reduce 把结果继续和序列的下一个元素做累积计算
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce
def add(x, y):
    return x + y

r = reduce(add, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(r)


L =['tom', 'cAT', 'TERRY', 'lUcY']
def title(x):
    return x.title()

print(list(map(title, L)))

# str api
str = "www.runoob.com"
print(str.upper())          # 把所有字符中的小写字母转换成大写字母
print(str.lower())          # 把所有字符中的大写字母转换成小写字母
print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写


def prod(x, y):
    return x * y

print(reduce(prod, [1, 2, 3, 4, 5]))