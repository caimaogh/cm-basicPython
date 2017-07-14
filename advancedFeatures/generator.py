#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 在Python中，一边循环一边计算的机制，称为生成器：generator
# 创建一个generator，第一种方法只要把一个列表生成式的[]改成()，就创建了一个generator
# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator
L1 = [x * x for x in range(10)]
print(L1)
g = (x * x for x in range(10))
print(g)
# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误
print(next(g), next(g), next(g), next(g), next(g), next(g), next(g), next(g), next(g), next(g))
# 使用for循环迭代generator, generator也是可迭代对象
g2 = (x * x for x in range(11))
for x in g2:  # 创建了一个generator后一般通过for循环来迭代，并且不需要关心StopIteration的错误
    print(x)

# 定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行


def fibonacci(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fibonacci(8)
for y in f:
    print(y)


def triangle(n):
    L = [1]
    m = 0
    while m <= n:
        yield L # generator生成器在遇到yield时返回,然后在下一次调用时从上次返回的yield语句处继续执行
        L = [L[x]+L[x+1] for x in range(len(L) - 1)]  #用从L list的第二个元素开始生成list
        L.insert(0, 1)
        L.append(1)
        m = m + 1

a = triangle(1)
for z in a:
    print(z)
