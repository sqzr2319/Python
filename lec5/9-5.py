#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/27 13:51
# @Author: ms169
import numpy as np
import pandas as pd

data = pd.read_csv("../data_20250625/CPI_202307-202407.csv", index_col=[0])
data.to_excel("9-5.xlsx")

data = pd.read_excel("9-5.xlsx", index_col=[0], header=[0])
print(data)
