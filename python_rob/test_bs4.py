#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   test_bs4.py
@Time    :   2021/04/12 22:07:52
@Author  :   Liu ChaoYang 
@Version :   1.0
@Contact :   2218932687@qq.com
'''

# here put the import lib

from bs4 import BeautifulSoup

file = open("./easy.html", "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")

# type(bs)表示整个文档


# 可以拿到被注释的的字符，输出不包含注释
# <a href="lcy2218.github.io">github</a>

# 找到第一个内容
print(bs.title)
print(bs.a)

print(type(bs.head))
<class 'bs4.element.Tag'>

# 拿到文字内容
print('-----'+bs.a.string+'---------')

# 拿到标签里的属性值
print(bs.a.attrs)
