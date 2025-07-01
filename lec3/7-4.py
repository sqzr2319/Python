#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/25 15:56
# @Author: ms169
import numpy as np

array = np.array([[8, 3, 2, 5], [6, 21, 15, 8], [34, 16, 20, 30]])

max_value = array.max(axis=0)
mean_value = array.mean(axis=0)

index = array[:, 1].argsort()
sorted_array = array[index]

new_array = array[np.where(array > 10)]
