#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   rob.py
@Time    :   2021/04/08 16:25:35
@Author  :   Liu ChaoYang 
@Version :   1.0
@Contact :   2218932687@qq.com
'''

# here put the import lib

'''
爬虫，按照一定规则，自动抓取互联网信息的程序或者脚本
模拟浏览器打开网页，获取想要的那部分数据
'''

#思路




import re   #正则表达式、文字匹配
from bs4 import BeautifulSoup #网页解析、获取数字
import urllib.request, urllib.error  #制定URL、获取网页数据
import xlwt   #进行excel操作
import sqlite3  #进行SQLite数据库操作

def main():
    baseUrl = "https://movie.douban.com/top250?strat="
    #1：爬取网页
    #2：解析数据   逐个解析数据
    dataList = getData(baseUrl)
    
    savePath = r"./data.xls"
    #3：保存数据
    saveData(savePath)


def getData(baseUrl):
    dataList = []

    return dataList


def saveData(savePath):
    pass



if __name__ == "__main__":
    main()
