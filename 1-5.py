#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/23 14:37
# @Author: ms169


list_a = ["Java", [80, 90, 100], "C++", "Python"]

list_a[2] = "C"  # 将 list_a 中的元素 "C++" 修改为 "C"
list_a.append("PHP")  # 将元素 "PHP" 插入到 list_a 的尾部
list_a[1][1:1] = [85, 89]  # 在 list_a 的元素 [80,90,100] 中，在 80 和 90 之间，一次性插入 85 和 89 两个值
list_b = list_a[1]  # 取出 list_a 中的元素 [80,85,89,90,100] 放入 list_b 中

# 在屏幕输出 list_b 的最大值、最小值、各元素之和
print("max=", max(list_b))
print("min=", min(list_b))
print("sum=", sum(list_b))
