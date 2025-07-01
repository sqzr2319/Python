#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/26 14:28
# @Author: ms169
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams["font.family"] = "FangSong"  # 设置字体为仿宋
matplotlib.rcParams["font.size"] = 14  # 设置字体大小为14

data = np.loadtxt("../data_20250625/iris_scatter.csv", delimiter=",")
x_data = data[:, 2]
y_data = data[:, 3]

plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data, s=4, c="r")
plt.title("鸢尾花数据集散点图")
plt.xlabel("花瓣长度(cm)")
plt.ylabel("花瓣宽度(cm)")

plt.grid(linestyle="--")
plt.show()
