#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/25 14:58
# @Author: ms169
import numpy as np

num_arr = np.linspace(0, 29, 30).reshape(10, 3)
arr_1 = num_arr[6:9, 0:3]
arr_2 = num_arr[0::2, 1:3]
arr_3 = num_arr[num_arr > 10]
arr_4 = num_arr[1::3, 1:3]
