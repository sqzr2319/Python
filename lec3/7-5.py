#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/25 16:24
# @Author: ms169
import numpy as np

array = np.arange(1001, 1023, 1)
np.random.shuffle(array)

x = np.random.choice(array, size=3, replace=True)
print("随机选择的元素：", x)
