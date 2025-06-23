#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/23 14:57
# @Author: ms169


# 元素正向索引和反向索引
tuple_a = ("Max", 28, "Boston", ["apple", "banana", "cherry"])

# 修改元组中的可变元素
tuple_a[3].append("blueberry")
print(tuple_a)

# 元组与列表互相转换
list_a = list(tuple_a)
print("list_a:", list_a)

obj_a = tuple(list_a)
print("type of obj_a", type(obj_a))

# 元组解包
name, age, city, favorite_fruits = tuple_a
print(name, age, favorite_fruits, sep="\n")
