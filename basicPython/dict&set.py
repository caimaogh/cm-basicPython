#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python内置了字典：dict(dictionary)在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
# dict的key必须是不可变对象
score = {'Tom':90,'Jerry':85,'Lucy':65}
print(score['Tom'])
# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值覆盖掉：
score['Rose'] = 100
print(score['Rose'])
score['Rose'] = 99
print(score['Rose'])
# 如果key不存在，dict就会报错;
#print(score['Tomas'])
# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
'Thomas' in score
# 二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
print(score.get('Tomas'))   #返回None的时候Python的交互式命令行不显示结果
print(score.get('Tomas',-1))

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
print(score)
score.pop('Tom')
print(score)


# Set是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
s = set([1,1,2, 2,3, 3])
print(s)
# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(4)
print(s)
# 通过remove(key)方法可以删除元素
s.remove(4)
print(s)
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([0,1,3,5,7,9])
s2 = set([0,2,4,6,8,10])
print(s1 & s2)
print(s1 | s2)