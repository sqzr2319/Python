#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/25 14:08
# @Author: ms169
import numpy as np

matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("秩：", matrix1.ndim)
print("形状：", matrix1.shape)
print("转置：", matrix1.T)
print("数据类型：", matrix1.dtype)
print("元素个数：", matrix1.size)

vector1 = np.arange(0, 12, 1)
print("数据类型：", vector1.dtype)
print("形状：", vector1.shape)

vector2 = np.linspace(0, 1, 20)

matrix2 = np.full((6, 7), 5)
