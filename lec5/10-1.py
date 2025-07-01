#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/27 15:04
# @Author: ms169
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../data_20250625/Iris_0815.csv", index_col=[0])
print(data.head())
print(data.tail())
print(data.describe())

data.drop_duplicates(inplace=True)
print("缺失值总数：", data.isnull().sum().sum())
print("各行缺失值个数：", data.isnull().sum(axis=1))

# 用同类均值填充缺失值
groups = data.groupby("Species")
for x in groups:  # x[0]是组名，x[1]是组数据
    values = x[1].mean().to_dict()
    x[1].fillna(value=values, inplace=True)
    data.update(x[1])

data.to_csv("10-1_fillna.csv")

data.plot(kind="box")
plt.show()

# 去除异常值
for col in ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]:
    q1 = data[col].quantile(0.25)
    q3 = data[col].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    data = data[(data[col] >= lower_bound) & (data[col] <= upper_bound)]

data.to_csv("10-1_cleaned.csv")
