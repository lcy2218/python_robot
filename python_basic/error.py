#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   error.py
@Time    :   2021/04/08 10:30:46
@Author  :   Liu ChaoYang 
@Version :   1.0
@Contact :   2218932687@qq.com
'''

# here put the import lib
'''
#捕获异常
try:
    print('-------1-------')
    f = open('123.txt', "r")  #打开了一个不存在的文件
    print('-------2-------')  #代码不被执行
except IOError:               #文件没找到，产生异常
    pass                      #产生异常后执行的代码


try:
    print(num)
#except IOError    #异常一致
except NameError:
    print("未定义变量")

try:
    f = open("123.txt", r)
    print(num)
except (NameError, IOError) as result:     #多种异常使用括号
    print("文件错误或者未定义变量")
    print(result)
'''
#Exception
import time
try:
    f = open("text.txt", "r")

    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print("文件关闭")

except Exception as result:
    print("产生异常")






