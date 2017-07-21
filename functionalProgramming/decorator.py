#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
def now():
    print('2017-07-21 16:21:22')

f = now
print(f())
# 函数对象有一个__name__属性，可以拿到函数的名字
print(now.__name__ , f.__name__)

