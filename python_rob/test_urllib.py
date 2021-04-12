#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   test_urllib.py
@Time    :   2021/04/11 22:59:38
@Author  :   Liu ChaoYang 
@Version :   1.0
@Contact :   2218932687@qq.com
'''

# here put the import lib
import urllib.request
import urllib.parse

#获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# #记得解码
# print(response.read().decode("utf-8"))


#获取一个post请求
data = bytes(urllib.parse.urlencode({"hello":"world"}), encoding = "utf-8")
response = urllib.request.urlopen("http://httpbin.org/post", data = data)
print(response.read().decode('utf-8'))