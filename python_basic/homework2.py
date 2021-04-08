#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   homework2.py
@Time    :   2021/04/07 22:38:23
@Author  :   Liu ChaoYang 
@Version :   1.0
@Contact :   2218932687@qq.com
'''

# here put the import lib

def myLine():
    #print("----------------------------------")
    print('-'*30)

def useLine(time):
    for i in range(0, time):
        myLine()

def addMun(a, b, c):
    return a + b + c

def spMun(a, b, c):
    t = addMun(a, b, c)
    return t // 3

print(addMun(12,24,133))
print(spMun(12,24,133))

