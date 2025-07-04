#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/7/3 23:54
# @Author: ms169
import numpy as np
import pandas as pd


# 数据处理类
class DataLoading:
    def __init__(self):  # 声明实例变量
        self.final_data = pd.DataFrame()

    def load_data(self, file_path):  # 逐个加载数据并剪裁、拼接
        data = pd.read_csv(file_path, skiprows=list(range(0, 16)), usecols=[3], sep="\t", header=None)
        data = data.to_numpy()
        data = data[0:1024000]
        data = data.reshape(-1, 1024)
        data = pd.DataFrame(data)
        self.final_data = pd.concat([self.final_data, data], ignore_index=True)

    def load_all_data(self):  # 加载所有数据
        self.load_data("gearbox_data/Chipped_20_0.csv")
        self.load_data("gearbox_data/Health_20_0.csv")
        self.load_data("gearbox_data/Miss_20_0.csv")
        self.load_data("gearbox_data/Surface_20_0.csv")
        return self.final_data
