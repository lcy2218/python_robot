#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   function.py
@Time    :   2021/04/07 22:31:28
@Author  :   Liu ChaoYang 
@Version :   1.0
@Contact :   2218932687@qq.com
'''

# here put the import lib

def printinfo():
    print("--------------------------------")
    print("|          write by lcy        |")
    print("--------------------------------")

#带参数的函数,返回值的
def add2Num(a, b):
    c = a + b
    return c

def divid(a, b):
    shang = a // b
    yushu = a % b
    return shang,yushu

# sh,yu = divid(5, 2)    #多个值来保存返回内容
# print("shang: %d, yu: %d"%(sh, yu))


'''
#局部变量
def test1():
    a = 300
    print('test1 -------- 修改前: a = %d'%a)
    a = 100
    print('test1 -------- 修改后: a = %d'%a)

def test2():
    a = 500
    print('test1 -------- 修改前: a = %d'%a)

test1()
test2()
'''