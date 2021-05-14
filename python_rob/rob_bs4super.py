#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   rob_bs4super.py
@Time    :   2021/04/25 14:57:16
@Author  :   Liu ChaoYang 
@Version :   1.0
@Contact :   2218932687@qq.com
'''

# here put the import lib

from bs4 import BeautifulSoup
import re

file = open("./easy.html", "rb")
html = file.read().decode('utf-8')
bs = BeautifulSoup(html, "html.parser")

# 文档的遍历
'''
print(bs.head.contents)
print('-'*30)
print(bs.head.contents[1])
'''

# 文档的搜索

#
'''
1. find_all()
'''

# # 字符串过滤：查找含有标签匹配的内容

'''
t_list = bs.find_all("a")
for t in t_list:
    print(t)
'''

# # 正则表达式：search方法匹配

'''
t_list = bs.find_all(re.compile("a"))
print(t_list[0],"\n")
print(t_list[1])
'''

# # 方法:传入一个函数，根据函数的要求来搜索

'''
def name_is_exists(tag):
    return tag.has_attr("name")

t_list = bs.find_all(name_is_exists)

print(t_list)
'''

#
'''
2. kwargs()  参数
'''

# # 使用参数来限制查找内容
'''
t_list = bs.find_all(id = "headeee")

t_list = bs.find_all(class_ = True)

for t in t_list:
    print(t)
'''

#
'''
3. text()  参数
'''

'''
#t_list = bs.find_all(text = "hao123")
#t_list = bs.find_all(text = ["hao123", "12", "中国人"])
t_list = bs.find_all(text = re.compile('\d'))  #应用正则表达式来查找包含特定文本的内容(标签里的字符串)
for t in t_list:
    print(t)
'''

#
'''
4. limit  参数
'''

'''
t_list = bs.find_all("div" , limit = 3)   #找出3个对应标签

for t in t_list:
    print(t)
'''

#
'''
5. css选择器
'''


#t_list = bs.select('head') #通过标签查找

# t_list = bs.select(".124") #通过类名查找

# t_list = bs.select("#div4") #通过ID查找

t_list = bs.select("head > title") #通过子标签查找
for t in t_list:
    print(t)



