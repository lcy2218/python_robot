#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   dict.py
@Time    :   2021/04/06 12:56:10
@Author  :   Liu ChaoYang 
@Version :   1.0
@Contact :   2218932687@qq.com
'''

# here put the import lib


#字典使用键值对
#字典的定义

'''
#字典的访问
print(info["name"])
print(info["age"])

#访问不存在的
#print(info["gender"])  #报错


print(info.get("gender"))  #使用get，没找到键会返回：None
print(info.get("gender", "mmmm"))  #没找到的时候设定默认值
'''

#增删改查
'''
info = {"name":"吴彦祖", "age":18}

#增
newID = input("请输入一个新的学号")
info["id"] = newID

print(info["id"])
'''
#删除  del  clear

'''
info = {"name":"吴彦祖", "age":18}
print(info)

del info["name"]
print(info)

del info
#print(info)   #报错
'''

#clear
'''
info = {"name":"吴彦祖", "age":18}
print(info)
info.clear()
print(info)
'''

#改
'''
info = {"name":"吴彦祖", "age":18}

info['age'] = 20

print(info)
'''

#查   便利
'''
info = {"name":"吴彦祖", "age":18, "id":1}
print(info.keys())
print(info.values())
print(info.items())
'''

info = {"name":"吴彦祖", "age":18, "id":1}
#便利所有的键
for key in info.keys():
    print(key)

for key,value in info.items():
    print("key = %s, value = %s"%(key, value))
print(type(info.items()))


myList = ['a', 'b', 'c', 'd']

print(enumerate(myList))
for i, x in enumerate(myList):   #使用枚举可以把myList拆开 拆成下标+元素
    print(i, x)
