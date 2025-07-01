#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/27 16:12
# @Author: ms169
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("10-1_cleaned.csv", index_col=[0])
columns = ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]  # 选中四个连续特征变量
data[columns] = (data[columns] - data[columns].mean()) / data[columns].std()
data.to_csv("10-2_standardized.csv")

data_encoded = pd.get_dummies(data, columns=["Species"])
data_encoded.to_csv("10-2_encoded.csv")
