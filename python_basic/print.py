#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   print.py
@Time    :   2021/04/05 12:22:50
@Author  :   Liu ChaoYang 
@Version :   1.0
@Contact :   2218932687@qq.com
'''
import keyword
# here put the import lib
print("helloword")

print(keyword.kwlist)


#格式化输出
a = 100
print("这是一个占位符%d"%a)
print("今天在%s,明天就会%s"%("下雨","天晴"))

#分割符号
print("www",'baidu','com',sep='.')
#结尾
print('i am',end='\t')
print('lcy',end='')
print('say,hello',end='\n')
