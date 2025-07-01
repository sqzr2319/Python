#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/30 10:02
# @Author: ms169
import numpy as np
from scipy.optimize import root


def func(vars):
    x, y, z = vars
    f1 = x + y ** 2 + z ** 3 - 14
    f2 = x * y * z - 6
    f3 = x ** 2 + y - z ** 3 - 3
    return [f1, f2, f3]


x_0 = np.array([1, 1, 1])  # 初始猜测值
sol = root(func, x_0)

print("Solution:", sol.x)
print("Success:", sol.success)
print("Message:", sol.message)

# 初始值设置为[1,1,1]时收敛，[-10,-10,-10]时不收敛
