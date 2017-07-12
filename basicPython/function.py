#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python内置了很多有用的函数，可供调用。要调用一个函数，需要知道函数的名称和参数
print(abs(-100))
# 调用函数的时候，如果传入的参数数量不对，会报TypeError的错误
# print(abs(-100,100))
# 如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError的错误
# print(abs('str'))
# max函数max()可以接收任意多个参数，并返回最大的那个
print(max(1,3,5,7,9))

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
#print(my_abs('33'))

#定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：ax2 + bx + c = 0的两个解。
import math
def quadratic(a,b,c):
    if a == 0:
        print('参数a错误,不能为0')
    else:
        y = b**2 - 4*a*c
        if y < 0:
            print('实数域内此方程无解!')
        elif y > 0:
            x1 = (-b + math.sqrt(b**2-4*a*c))/2*a
            x2 = (-b - math.sqrt(b**2-4*a*c))/2*a
            return x1,x2
        else:
            x1 = x2 = -b/2*a
            return x1,x2


a = quadratic(1,2,1)
print(a)












