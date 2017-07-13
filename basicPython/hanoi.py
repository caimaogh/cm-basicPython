#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 汉诺塔递归函数

def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')


def hanoi(n, a='A', b='B', c='C'):
    if n == 1:
        print(a, '--->', c)
    else:
        hanoi(n-1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n-1, b, a, c)




print(hanoi(2))

