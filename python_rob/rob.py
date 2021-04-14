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




import re   #正则表达式、文字匹
from bs4 import BeautifulSoup #网页解析、获取数字
import urllib.request, urllib.error  #制定URL、获取网页数据
import xlwt   #进行excel操作
import sqlite3  #进行SQLite数据库操作

def main():
    baseUrl = "https://movie.douban.com/top250?strat="
    #1：爬取网页
    #2：解析数据   逐个解析数据
    # dataList = getData(baseUrl)
    # savePath = r"./data.xls"
    #3：保存数据
    # saveData(savePath)

    askUrl(baseUrl)

#2：解析数据   逐个解析数据
def getData(baseUrl):
    dataList = []
    for i in range(0, 10):
        #https://movie.douban.com/top250?strat=1..2..3..4..5
        #拼接字符串
        url = baseUrl + str(i*25)
        html = askUrl(url)      #保存获取到的网页源码
        #获取网页后开始解析数据
        
    return dataList

#1：爬取网页
def askUrl(url):
    #模拟浏览器头部信息、向豆瓣发送信息
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
    }
    request = urllib.request.Request(url, headers = head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        print(html)
    #捕获错误
    except urllib.error.URLError as result:
        #打印状态码
        if hasattr(result, "code"):
            print(result.code)
        #打印失败原因
        if hasattr(result, "reason"):
            print(result.reason)

    return html

def saveData(savePath):
    pass



if __name__ == "__main__":
    main()
