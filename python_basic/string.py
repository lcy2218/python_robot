#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   string.py
@Time    :   2021/04/05 21:12:24
@Author  :   Liu ChaoYang 
@Version :   1.0
@Contact :   2218932687@qq.com
'''

# here put the import lib
'''
word = '字符串'
sentence = "这是个句子"
paragraph = """
这是个段落
可以又多行组成
"""

print(word)
print(sentence)
print(paragraph)
'''

my_str1 = "i am a student"
print(my_str1)
#my_str2 = 'i'm a student'
my_str2 = 'i\'m a student'  #转义字符

my_str = "he said \"he like you\""   #转义字符
my_str = 'he said "he like you"'   #转义字符
print(my_str)

'''
常用
\'
\"
\n
\t
\r  回车
'''

str = "chengdu"   #把str看出数组

# print(str)
# print(str[0:6])   #[起始位置:结束位置:步进值]
# print(str[0:6:2])

# print(str[5:])
# print(str[:5])

# print(str + ",hello")

# print('\n')

# print(str * 3)

print("hello\nchengdu")
print(r"hello\nchengdu")   #不进行转义 显示原始字符串
'''
bytes.decode(encoding='utf-8',errors='strict')
join()
spilt()
'''