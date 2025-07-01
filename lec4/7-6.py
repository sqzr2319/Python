#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/26 08:51
# @Author: ms169
import numpy as np

scores = np.loadtxt("../data_20250625/scores.csv", delimiter=",", dtype=int)

column_max = scores.max(axis=0)
print("Column-wise maximum scores:", column_max)
column_min = scores.min(axis=0)
print("Column-wise minimum scores:", column_min)
column_mean = scores.mean(axis=0)
print("Column-wise mean scores:", column_mean)
column_var = scores.var(axis=0)
print("Column-wise variance of scores:", column_var)

row_mean = scores.mean(axis=1)
print("Row-wise mean scores:", row_mean)

scores[:, 0] = np.around((scores[:, 0] ** 0.5) * 10)
print("Updated scores after transformation on first column:", scores)

row_mean = scores.mean(axis=1)
scores = scores[row_mean.argsort()]
np.savetxt("7-6.csv", scores, delimiter=",", fmt="%d")
