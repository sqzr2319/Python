#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/27 10:29
# @Author: ms169
import numpy as np
import pandas as pd

data = pd.read_csv("../data_20250625/Iris.csv")
print(data.head(5))

data.sort_values(by="SepalWidth", ascending=False, inplace=True)  # 用inplace=True修改原数据
print(data)

columns = ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]
print(data[columns].max())
print(data[columns].min())
print(data[columns].mean())
print(data[columns].median())
print(data[columns].corr())

groups = data.groupby("Species")
print(groups.count())
print(groups.max())
print(groups.min())
print(groups.mean())
