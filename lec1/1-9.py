#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/23 16:24
# @Author: ms169


# 以书院信息表中的书院英文简称为 key，以中文全名为 value，创建字典对象
college_dict = dict([("xyc", "新雅书院"), ("zlc", "致理书院"), ("rxc", "日新书院"), ("wyc", "未央书院"),
                     ("twc", "探微书院"), ("xjc", "行健书院"), ("qzc", "求真书院"), ("dsc", "笃实书院")])

# 使用 for 循环语句同时遍历字典对象的 key,value（在屏幕依次输出 key 和对应的 value）
for key, value in college_dict.items():
    print(key, value)

# 使用 for 循环语句，只遍历字典对象的 value
for value in college_dict.values():
    print(value)
