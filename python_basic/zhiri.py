#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   zhiri.py
@Time    :   2021/04/14 17:51:56
@Author  :   Liu ChaoYang 
@Version :   1.0
@Contact :   2218932687@qq.com
'''

# here put the import lib

import random
list_61 = ['柳朝洋', '雷盛昆', '程煌', '罗勇', '候忠佳', '刘振宇']

for i in range(1, 6):
    delet = random.choice(list_61)
    print("周%d"%i, delet)
    list_61.remove(delet)


print("周5", list_61.pop())