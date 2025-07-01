#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/30 08:47
# @Author: ms169
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("../data_20250625/cleaned.csv", index_col=[0])
groups = data.groupby("Species")

for name, group in groups:
    group.drop(columns=["Species"], inplace=True)  # 删除Species列
    # 绘制直方图
    group.hist(bins=20)
    plt.tight_layout()
    plt.savefig(f"10-3_{name}_hist.png")  # 保存直方图
    plt.show()
    # 绘制散点图
    group.plot(kind="scatter", x="SepalLength", y="PetalLength")
    plt.tight_layout()
    plt.savefig(f"10-3_{name}_scatter.png")  # 保存散点图
    plt.show()

# 计算相关系数矩阵
corr_matrix = data[["SepalLength", "SepalWidth", "PetalLength", "Species"]].corr()
print(corr_matrix)
selected_data = data[["SepalLength", "SepalWidth", "PetalLength", "Species"]]
selected_data.to_csv("10-3.csv")
