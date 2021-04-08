#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   homwork3.py
@Time    :   2021/04/08 10:51:11
@Author  :   Liu ChaoYang 
@Version :   1.0
@Contact :   2218932687@qq.com
'''

# here put the import lib
import os
def creatFile():
    try:
        f = open("gushi.txt", "w")
        text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
        """
        f.write(text)
        f.close()

        f = open("gushi.txt", 'r')
        content = f.readlines()
        # for temp in content:
        #     print(temp)
        f.close()

    except Exception as result:
        print("产生异常")

def copyFile():
    try:
        f = open("gushi.txt", "r")
        copyStr = f.readlines()
        copyFile = open ("copy.txt", "w")
        for str in copyStr:
            copyFile.write(str)

        #想读取文件内容得从只读模式下打开
        copyFile = open("copy.txt", "r")
        copyContent = copyFile.readlines()
        for temp in copyContent:
            print(temp, end='')
        f.close()
        copyFile.close()
    except Exception as result:
        print("产生了奇怪的问题")


creatFile()
copyFile()