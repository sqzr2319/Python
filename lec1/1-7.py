#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/23 15:33
# @Author: ms169


lst1 = [1, 2, 3, 5, 6, 3, 2]
lst2 = [2, 5, 7, 9]

# 使用 lst1 和 lst2 中的元素创建集合 set1 和 set2
set1 = set(lst1)
set2 = set(lst2)

print(set1 & set2)  # 判断哪些整数既在 set1 中，也在 set2 中，输出至屏幕
print(set1 - set2)  # 哪些整数在 set1 中，不在 set2 中，输出至屏幕
print(set1 | set2)  # 两个集合一共有哪些整数，输出至屏幕
