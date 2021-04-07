#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   break_continue.py
@Time    :   2021/04/05 20:20:45
@Author  :   Liu ChaoYang 
@Version :   1.0
@Contact :   2218932687@qq.com
'''

# here put the import lib

i = 0
while i < 10:
    i += 1
    print('-'*30)
    if i == 5:
        break
    print(i)

i = 0
while i < 10:
    i += 1
    print('-'*30)
    if i == 5:
        continue   #跳出当前循环，执行下一次循环
    print(i)

#99乘法表
for i in range(1, 10, 1):
    for j in range(1, 10, 1):
        if i >= j:
            print('%d*%d=%d'%(i,j,i*j), end='\t')
    print('\n')