#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素
classmates = ['Tom','Jerry','LiLei','HanMeiMei','Lucy']
print(classmates)

# 变量classmates就是一个list。用len()函数可以获得list元素的个数：
print(len(classmates))
# 用索引来访问list中每一个位置的元素，索引是从0开始的：
print(classmates[0],classmates[1],classmates[2],classmates[3],classmates[4])
# 当索引超出了范围时，Python会报IndexError: list index out of range错误，最后一个元素的索引是len(classmates) - 1
#print(classmates[5])
# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
print(classmates[-1])
# list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classmates.append('Lili')
# 也可以把元素插入到指定的位置，比如索引号为1的位置：
classmates.insert(2,'SpongeBob')
print('insert()后',classmates)
# 要删除list末尾的元素，用pop()方法：
classmates.pop()
print('pop()后',classmates)
# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmates.pop(3)
print('pop(3)后',classmates)
# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[1] = 'Sarah'
# list里面的元素的数据类型也可以不同,list元素也可以是另一个list