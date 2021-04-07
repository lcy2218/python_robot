#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   tuple.py
@Time    :   2021/04/06 12:23:41
@Author  :   Liu ChaoYang 
@Version :   1.0
@Contact :   2218932687@qq.com
'''

# here put the import lib

'''
tup1 = ()   #创建空的元组
print(type(tup1))

# tup2 = (50)  #<class 'int'>
tup2 = (50, )
tup2 = (50, 60, 70)
print(type(tup2))  #<class 'tuple'>
'''

'''
tup1 = ("abc", "def", 2000, 2020, 333, 444, 555, 666)

print(tup1[0])
print(tup1[-1])
print(tup1[1:5])  #左闭右开
'''

'''
#增(连接)

tup1 = (12, 34, 56)
tup2 = ("abc","xyz")

tup = tup1 + tup2

print(tup)
'''

#删()
tup1 = (12, 34, 56)
print(tup1)
del tup1          #删除了整个元组
print("删除后:")
#print(tup1)


#改
tup1 = (12, 34, 56)

#tup1[0] = 100    #报错，不允许修改

