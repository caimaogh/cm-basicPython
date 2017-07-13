#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python内置了很多有用的函数，可供调用。要调用一个函数，需要知道函数的名称和参数
print(abs(-100))
# 调用函数的时候，如果传入的参数数量不对，会报TypeError的错误
# print(abs(-100,100))
# 如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError的错误
# print(abs('str'))
# max函数max()可以接收任意多个参数，并返回最大的那个
print(max(1, 3,5,7,9))

# Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数
print(int('123'),str(123),float('1.23'),bool(1),bool())
# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs
print(a(-22))

# hex()函数把一个整数转换成十六进制表示的字符串
print('17的十六进制表达式:',str(hex(17)))


# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回
# 函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回;如果没有return语句，函数执行完毕后也会返回结果，只是结果为None
# return None可以简写为return
# 在Python交互环境中定义函数时，注意Python会出现...的提示。函数定义结束后需要按两次回车重新回到>>>提示符下
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-99))
# print(my_abs('33'))

# 定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：ax2 + bx + c = 0的两个解。
import math


def quadratic(a, b, c):
    if a == 0:
        print('参数a错误,不能为0')
    else:
        y = b**2 - 4*a*c
        if y < 0:
            print('实数域内此方程无解!')
        elif y > 0:
            x1 = (-b + math.sqrt(b**2-4*a*c))/2*a
            x2 = (-b - math.sqrt(b**2-4*a*c))/2*a
            return x1, x2
        else:
            x1 = x2 = -b/2*a
            return x1, x2


a = quadratic(1,2,1)
print(a)

# Python的函数定义除了正常定义的必选参数外，还可以使用默认参数(默认参数必须指向不变对象)、可变参数和关键字参数


def power(x, n):   # x和n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5, 3))


# 第二个参数n是默认参数，默认参数可以简化函数的调用 ,必选参数在前，默认参数在后，否则Python的解释器会报错
def power2(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power2(5), power2(5, 4))

# 有多个默认参数时，调用的时候，既可以按顺序提供默认参数;也可以不按顺序提供部分默认参数，需要把参数名写上
def enroll(name, gender, age=6, city='Chengdu'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

print(enroll('Tom', 'M', '12'))
print(enroll('Jerry', 'F', city='Beijing'))

# 可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号,把list或tuple的元素变成可变参数传进去
def calc(*numbers):
    sum = 0
    express = ''
    for n in numbers:
        sum = sum + n*n
        express = express + str(n) + str(2) + '+'
    return sum, express

print(calc(1, 2, 3))
num = [1, 2, 3]
num2 = (1, 2, 3)
# Python允许在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
print(calc(*num))
print(calc(*num2))

# 关键字参数允许传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict;**kw表示关键字参数
# 命名关键字参数 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错


# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数



# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数
def fact(n):
    if n==1:
        return 1
    return  n * fact(n - 1)

print(fact(100))
# 使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，
# 每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
print(fact(1000))
# 解决递归调用栈溢出的方法是通过尾递归优化，尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。















