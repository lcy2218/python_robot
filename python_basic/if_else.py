#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   if_else.py
@Time    :   2021/04/05 16:19:59
@Author  :   Liu ChaoYang 
@Version :   1.0
@Contact :   2218932687@qq.com
'''

# here put the import lib
#同一个程序段缩进得相同
import random

x = random.randint(0,2)  #随机生成0-2之间的数


if True :
    print('true')
else :
    print('flase')

#switch
score = 88
if score >= 90 and score <= 100:
    print('本次为A')
else :
    if score >= 80 and score <= 90:
        print('本次为B')
    else :
        print('本次为E')


if score >= 90 and score <= 100:
    print('本次为A')
elif score >= 80 and score <= 90:
    print('本次为B')
else:
    print('本次为E')

#if_else嵌套

xingBie = 1  
danShen = 1

if xingBie == 1:
    print('男生')
    if danShen == 1:
        print('我给你介绍一个?')
    else:
        print('你给我介绍一个?')
else:
    print('女生')
    if danShen == 1:
        print('给你介绍个？')
    else:
        print('继续单着吧!')




