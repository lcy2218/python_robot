#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   file.py
@Time    :   2021/04/08 10:05:43
@Author  :   Liu ChaoYang 
@Version :   1.0
@Contact :   2218932687@qq.com
'''

# here put the import lib

'''
f = open('test.txt', 'w')  #不存在会新建, 默认为只读
f.write("hello world, i am here")  #将字符串写入文件中

f.close()  #关闭文件
'''

#read方法定位在文件头部
'''
f = open("test.txt", "r")

content = f.read(5)   #顺序读写
print(content)
content = f.read(5)   #每次往后移5个
print(content)
f.close()
'''

f = open('test.txt', 'r')
content = f.readlines()   #一次读取全部文件为列表， 每行一个字符串元素
print(content)

f.close()
i = 1
for temp in content:
    print('行号%d:内容%s'%(i, temp))
    i += 1


#readline()从头开始向后读写
f = open('test.txt', 'r')
content = f.readline()
print("1:%s"%content, end="")
content = f.readline()
print("2:%s"%content, end="")
content = f.readline()
print("3:%s"%content, end="")
f.close()

'''
r  ------只读
rb ------二进制只读
wb ------二进制写
'''

import os
os.rename("text.txt", "text.txt")
print(os.getcwd())


'''
获取当前目录：os.getcwd()
获取目录列表: os.listdir()
'''