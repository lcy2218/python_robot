#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   list.py
@Time    :   2021/04/05 21:52:15
@Author  :   Liu ChaoYang 
@Version :   1.0
@Contact :   2218932687@qq.com
'''

# here put the import lib

# namelist = ["小张", "小王", "小李"] 
#print(namelist[1])

# testlist = [11241, "测试"]  #列表可以存储混合类型
# print(type(testlist[0]),type(testlist[1]),sep='\t')

'''
for name in namelist:
    print(name)


length = len(namelist)
i = 0
while i < length:
    print(namelist[i])
    i += 1
'''

#增加列表元素
'''
print("--------------增加前 名单列表的数据-------------")
for name in namelist:
    print(name)

nametemp = input("请输入添加学生的姓名:")
namelist.append(nametemp)   #在末尾 追加元素

print("--------------增加后 名单列表的数据-------------")
for name in namelist:
    print(name)


a = [1, 2]
b = [3, 4]
a.append(b)   #把b列表当作一个元素加入a列表中

print(a)

a.extend(b)   #将b列表中的每个元素  拆散了    加到a列表中

print(a)

c = [0,1,2]
c.insert(1, 3)  #第一个变量标识下标，第二个变量表示元素(对象)    指定下标位置插入元素
print(c)
'''


#删除 del pop  remove
'''
movieName = ["加勒比海盗", "骇客帝国", "第一滴血", "指环王", "速度与激情"]

print("--------------删除前 名单列表的数据-------------")
for name in movieName:
    print(name)

#del movieName[2]  #在指定位置删除一个元素
#movieName.pop()    #弹出最后一个元素，并输出
movieName.remove("指环王")    #从前往后遍历，删除第一个

print("--------------删除后 名单列表的数据-------------")
for name in movieName:
    print(name)
'''

#改
'''
movieName = ["加勒比海盗", "骇客帝国", "第一滴血", "指环王", "速度与激情"]
print("--------------删除前 名单列表的数据-------------")
for name in movieName:
    print(name)

movieName[1] = "变形金刚"   #指定下标修改

print("--------------删除后 名单列表的数据-------------")
for name in movieName:
    print(name)
'''

#查  : in/ not in
'''
movieName = ["加勒比海盗", "骇客帝国", "第一滴血", "指环王", "速度与激情"]
findName = input("请输入电影名称:")

if findName in movieName:   #判断是否在其中
    print("查找成功:%s"%findName)
else:
    print("未找到:%s"%findName)
'''

'''
aList = ["x", "b", "c", "d", "e", "a", "h"]

#查找指定下标范围的元素，返回对应的下标
print(aList.index("a", 0, 6))   #不在 0 - 6 中会报错
print(aList.index("a", 0, 5))   #左闭右开

print(aList.count("c"))    #统计元素出现几次
'''

#排序和反转
'''
bList = [1, 4, 2, 3]

print(bList)
bList.reverse()    #将列表所有元素反转
print(bList)
bList.sort()       #排序,升序
print(bList)
bList.sort(reverse = True)  #排序, 降序
print(bList)
'''

#嵌套,类似二维列表
'''
schoolName = [[],[],[]]     #三个元素都是列表

schoolName = [["北京大学", "清华大学"], ["南开大学", "天津大学", "天津师范大学"], ["山东大学", "中国海洋大学"]]

print(schoolName[0])
print(schoolName[0][0])
'''

#三个办公室  8个老师 随机分配到三个办公室里
# import random

# officeList = [[], [], []]

# nameList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# for name in nameList:
#     index = random.randint(0, 2)    #在0,2中随机取值
#     officeList[index].append(name)  #把nameList中的值 加入到officeList中

# i = 1
# for office in officeList:
#     print("%d号办公室的人数为: %d人"%(i, len(office)))
#     i += 1
#     for name in office:
#         print("%d号办公室的老师为:%s"%(i, name))
#     print('-'*20)


#三个办公室  8个老师 随机分配到三个办公室里
import random

myOfficeList = [[], [], []]

myTeachList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for teach in myTeachList:
    myRandom = random.randint(0, 2)
    myOfficeList[myRandom].append(teach)

num = 1
for office in myOfficeList:
    print('%d号办公室有%d个老师'%(num, len(office)))
    num += 1
    for teacher in office:
        print("老师", teacher, end="\t")
    print('\n')


