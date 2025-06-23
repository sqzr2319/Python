#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/23 10:24
# @Author: ms169


def print_str(var_a):
    """输出对象的值及其三个属性，
       可使用help查看此文档字符串
    """
    print("值：", var_a)  # 输出对象的值
    print("内存地址：", id(var_a))
    print("对象类型：", type(var_a))


# 创建了一个str对象
var_str = "Hello Python!"
print_str(var_str)
