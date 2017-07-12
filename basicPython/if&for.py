#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 根据Python的缩进规则，如果if语句判断是True，就执行缩进的语句,否则执行else以下缩进的语句
# if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
age = 3
if age >= 18:   #注意不要少写了冒号:
    print('Your age is ',age,',Hello adult')
elif age >= 6:  #elif是else if的缩写，完全可以有多个elif
    print('Your age is ',age,',Hello teenager!')
else:           #注意不要少写了冒号:
    print('Your age is ',age,',Hello kid!')

#name = input('What\'s your name?\n')
#high = float(input('please input you high!\n'))
#weight = float(input('please input you weight!\n'))
#bmiIdex = weight/(high**2)
#if bmiIdex<=18.5:
#    print('Please attention ',name,',your BMI:%.1f' %bmiIdex,'过轻')
#elif bmiIdex<=25:
#   print('Congratulation  ',name,',your BMI:%.1f' %bmiIdex,'正常')
#elif bmiIdex<=28:
#   print('Sorry  ',name,',your BMI:%.1f' %bmiIdex,'过重')
#elif bmiIdex<=32:
#   print('Unfortunately ',name,',your BMI:%.1f' %bmiIdex,'肥胖')
#else:
#   print('very bad ',name,',your BMI:%.1f' %bmiIdex,'严重肥胖')

# for循环
# Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list
sum = 0
for x in list(range(101)):
    sum = sum + x
print('sum=',sum)

# while循环
total = 0
n = 99
while n>0:
    total = total + n
    n = n - 2
print('total=',total)

# break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。