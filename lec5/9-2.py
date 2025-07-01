#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/27 09:27
# @Author: ms169
import numpy as np
import pandas as pd

data = {"GDP": [17.79, 27.36, 2.02, 3.03, 3.34],
        "Pop": [14.12, 3.32, 1.43, 0.68, 0.67],
        "Area": [960, 983, 1710, 55, 24]}
x_index = ["China", "USA", "Russia", "France", "UK"]
dataframe = pd.DataFrame(data, index=x_index)

print(dataframe.iloc[1:4, 1:3])
print(dataframe[(dataframe["GDP"] > 10) & (dataframe["Area"] > 900)])

dataframe["CPI"] = [1.97, 8.0, 6.69, 5.22, 7.92]
print(dataframe)

dataframe["Area"] = dataframe["Area"].astype(float)  # 将Area列转换为浮点数类型
dataframe.loc["UK", "Area"] = 24.41
dataframe.drop("GDP", axis=1, inplace=True)
