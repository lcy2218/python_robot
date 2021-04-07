#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   circulate.py
@Time    :   2021/04/05 19:11:49
@Author  :   Liu ChaoYang 
@Version :   1.0
@Contact :   2218932687@qq.com
'''

# here put the import lib
'''
for i in range(5):
    print(i)
'''

# for i in range(0, 10, 3): #从0到10，步进值为3
#     print(i)

# print('\n')
# for i in range(-10, -100, -30):
#     print(i)
'''
# name = 'chengdu'

 for x in name:
     print(x,end='\t')
 print('\n')

 a = ['aa', 'bb', 'vv', 'cc']
 for i in range(len(a)):
     print(i,a[i])
'''

i = 0
while i < 5:
    print('当前是第%d次执行循环'%(i+1))
    print('i = %d'%i)
    i += 1

#1到100求和
i = 1
user_sum = 0
while i <= 100:
    user_sum += i
    i += 1
print(user_sum)

#不满足while后 执行else中的内容
count = 0
while count < 5:
    print(count,'小于5')
    count += 1
else:
    print(count,'大于或等于5')