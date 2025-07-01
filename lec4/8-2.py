#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/26 11:11
# @Author: ms169
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("../data_20250625/iris_scatter.csv", delimiter=",", dtype=float)

plt.figure(figsize=(8, 6))

# 绘制花萼长度的直方图
plt.subplot(2, 2, 1)
n, bins, patches = plt.hist(data[:, 0], bins=20)
plt.xlabel("花萼长度", fontproperties="FangSong", fontsize=14)
plt.ylabel("频数", fontproperties="FangSong", fontsize=14)
plt.title("花萼长度直方图", fontproperties="FangSong", fontsize=14)
print("花萼长度直方图的频数：", n)
print("花萼长度直方图的区间：", bins)

# 绘制花萼宽度的直方图
plt.subplot(2, 2, 2)
n, bins, patches = plt.hist(data[:, 1], bins=20)
plt.xlabel("花萼宽度", fontproperties="FangSong", fontsize=14)
plt.ylabel("频数", fontproperties="FangSong", fontsize=14)
plt.title("花萼宽度直方图", fontproperties="FangSong", fontsize=14)
print("花萼宽度直方图的频数：", n)
print("花萼宽度直方图的区间：", bins)

# 绘制花瓣长度的直方图
plt.subplot(2, 2, 3)
n, bins, patches = plt.hist(data[:, 2], bins=20)
plt.xlabel("花瓣长度", fontproperties="FangSong", fontsize=14)
plt.ylabel("频数", fontproperties="FangSong", fontsize=14)
plt.title("花瓣长度直方图", fontproperties="FangSong", fontsize=14)
print("花瓣长度直方图的频数：", n)
print("花瓣长度直方图的区间：", bins)

# 绘制花瓣宽度的直方图
plt.subplot(2, 2, 4)
n, bins, patches = plt.hist(data[:, 3], bins=20)
plt.xlabel("花瓣宽度", fontproperties="FangSong", fontsize=14)
plt.ylabel("频数", fontproperties="FangSong", fontsize=14)
plt.title("花瓣宽度直方图", fontproperties="FangSong", fontsize=14)
print("花瓣宽度直方图的频数：", n)
print("花瓣宽度直方图的区间：", bins)

plt.savefig("8-2.jpg")
plt.tight_layout()
plt.show()
