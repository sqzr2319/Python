#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/26 15:23
# @Author: ms169
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams["font.family"] = "FangSong"  # 设置字体为仿宋
matplotlib.rcParams["font.size"] = 14  # 设置字体大小为14

data = plt.imread("../data_20250625/panda.jpg").copy()
plt.imshow(data)
plt.show()

data[:, :, 1] = 0
data[:, :, 2] = 0
plt.imshow(data)
plt.show()

plt.imsave("8-7.jpg", data)
