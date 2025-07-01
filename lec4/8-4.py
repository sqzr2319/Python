#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/26 14:01
# @Author: ms169
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams["font.family"] = "FangSong"  # 设置字体为仿宋
matplotlib.rcParams["font.size"] = 14  # 设置字体大小为14

x_label = ["中国", "美国", "俄罗斯", "法国", "英国", "其他"]
y_data = [17.73, 23.03, 1.78, 2.94, 3.19, 47.43]

plt.figure(figsize=(8, 6))
plt.pie(y_data, labels=x_label, explode=(0.1, 0, 0, 0, 0, 0), autopct="%1.1f%%")
plt.title("2024年部分国家GDP数据（万亿美元）")

plt.show()
