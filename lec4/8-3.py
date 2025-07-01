#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/26 13:39
# @Author: ms169
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams["font.family"] = "FangSong"  # 设置字体为仿宋
matplotlib.rcParams["font.size"] = 14  # 设置字体大小为14

x_label = ["中国", "美国", "俄罗斯", "法国", "英国"]
y_data = [14.25, 3.41, 1.43, 0.67, 0.68]

plt.figure(figsize=(8, 6))
plt.bar(x_label, y_data, color='blue')
plt.ylabel("人口（亿）")
plt.title("2024年部分国家人口数据")

for i, v in enumerate(y_data):
    plt.text(i, v + 0.1, f"{v:.2f}", ha='center', va='bottom', fontsize=12)

plt.show()
