#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/27 11:20
# @Author: ms169
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif'] = "FangSong"  # 设置中文字体
matplotlib.rcParams['font.size'] = 14  # 设置字体大小

gdp_data = pd.read_csv("../data_20250625/GDP_2003_2023.csv", index_col=[0])
gdp_data.columns = ["中国", "美国", "俄罗斯", "法国", "英国"]
gdp_data.plot(kind="line", xlabel="年份", ylabel="GDP（万亿）", title="部分国家GDP（2003-2023）")
plt.show()

pop_data = pd.read_csv("../data_20250625/GDP_POP_2023.csv", index_col=[0], usecols=["Country", "GDP", "Pop"])
pop_data.index = ["中国", "美国", "俄罗斯", "法国", "英国"]
pop_data.columns = ["GDP", "人口"]
pop_data.plot(kind="bar", ylabel="GDP（万亿）/人口（亿）", title="部分国家GDP和人口（2023）", rot=0)
plt.show()

iris_data = pd.read_csv("../data_20250625/iris_hist.csv")
iris_data.columns = ["花萼长度", "花萼宽度", "花瓣长度", "花瓣宽度"]
iris_data.hist(bins=20)
plt.tight_layout()
plt.show()
