#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/23 14:07
# @Author: ms169


thu_url = "www.tsinghua.edu.cn"

print(thu_url[4:-7])  # 第 4 到第 -7 个字符
print(thu_url[0:])  # 截取所有字符
print(thu_url * 2)  # 输出字符串两次
str_list = thu_url.split('.')
print(str_list)
print(thu_url.upper())  # 字母全大写
print(thu_url.title())  # 单词首字母大写

print(thu_url.find("tsinghua"))  # 字符串查找
ie_url = thu_url.replace("tsinghua", "tsinghua.ie")

print(ie_url + "\n工业工程系欢迎您！")  # 用'\'转义
