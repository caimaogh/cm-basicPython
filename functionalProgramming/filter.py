#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python内建的filter()函数用于过滤序列。filter()也接收一个函数和一个序列。
# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。


def is_odd(x):
    return x % 2 == 1

print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数


def is_palindrome(n):
    return str(n) == str(n)[::-1]

print(list(filter(is_palindrome, range(1,1000))))