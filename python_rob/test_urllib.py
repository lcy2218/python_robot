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
import urllib
from urllib import parse
from urllib import request

#获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# #记得解码
# print(response.read().decode("utf-8"))


#获取一个post请求   需要用POST来封装
'''
data = bytes(urllib.parse.urlencode({"hello":"world"}), encoding = "utf-8")
response = urllib.request.urlopen("http://httpbin.org/post", data = data)
print(response.read().decode('utf-8'))
'''

#超时处理   try  except
'''
try:
    response = urllib.request.urlopen("http://httpbin.org/get", timeout = 1)
    print(response.read().decode('utf-8'))
except urllib.error.URLError as result:
    print("timeout")
'''

'''
response = urllib.request.urlopen("http://httpbin.org/get", timeout = 1)
#print(response.status)
responseList = response.getheaders()

for key in responseList:
    print(key)

print(response.getheader("Server"))
'''

'''
url = "http://httpbin.org/post"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    }
#把键值对 'name':'lcy' 放入data中
data = bytes(urllib.parse.urlencode({'name':'lcy'}), encoding = 'utf-8')
req = urllib.request.Request(url = url, data = data, headers = headers, method = "POST")
response = urllib.request.urlopen(req)

print(response.read().decode('utf-8'))
'''
url = "https://douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    }
#把键值对 'name':'lcy' 放入data中
#data = bytes(urllib.parse.urlencode({'name':'lcy'}), encoding = 'utf-8')
req = urllib.request.Request(url = url, headers = headers, method = "GET")
response = urllib.request.urlopen(req)

print(response.read().decode('utf-8'))