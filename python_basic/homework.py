#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   homework.py
@Time    :   2021/04/05 18:56:12
@Author  :   Liu ChaoYang 
@Version :   1.0
@Contact :   2218932687@qq.com
'''

# here put the import lib

#简易石头剪刀布
import random

com_random = random.randint(0,2)
user_input = int(input('请输入石头(0)剪刀(1)布(2):'))


if com_random == 0:
    com_output = '石头'
elif com_random == 1:
    com_output = '剪刀'
else:
    com_output = '布'

print('电脑出的是:%s'%com_output)

if user_input == com_random:
    print('本次平局')

if user_input == 0 and com_random == 1:
    print('你赢了')
elif user_input == 0 and com_random == 2:
    print('电脑赢了')
elif user_input == 1 and com_random == 0:
    print('电脑赢了')
elif user_input == 1 and com_random == 2:
    print('你赢了')
elif user_input == 2 and com_random == 0:
    print('你赢了')
elif user_input == 2 and com_random == 1:
    print('电脑赢了')
