#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回

# 在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 2, 3, 4, 5)
# 调用lazy_sum()时，返回的并不是求和结果，而是求和函数
# 调用函数f时，才真正计算求和的结果
print(f, f())
# 调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
f1 = lazy_sum(1, 2, 3, 4, 5)
f2 = lazy_sum(1, 2, 3, 4, 5)
print(f1 == f2)

# 返回函数不要引用任何循环变量，或者后续会发生变化的变量
