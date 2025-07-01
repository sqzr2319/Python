#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/7/1 09:00
# @Author: ms169
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("../data_20250625/appended.csv")

# 将数据集划分为特征和目标变量
X_data = data.drop("Serious", axis=1)
Y_data = data["Serious"]

# 将数据集划分成训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_data, Y_data, test_size=0.3, random_state=42)

# 进行k折交叉验证
model = RandomForestClassifier(n_estimators=100, random_state=42)
scores = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
print("交叉验证得分：", scores)
print("平均交叉验证得分：", np.mean(scores))

# 选取不同分类模型，网格搜索
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}
grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)
print("最佳参数：", grid_search.best_params_)

# 输出最佳模型的得分
best_score = grid_search.best_score_
print("最佳模型的交叉验证得分：", best_score)

# 换用逻辑回归，网格搜索
param_grid_lr = {
    'C': [0.01, 0.1, 1, 10],
    'penalty': ['l2']
}
grid_search_lr = GridSearchCV(LogisticRegression(random_state=42, max_iter=1000), param_grid_lr, cv=5,
                              scoring='accuracy', n_jobs=-1)
grid_search_lr.fit(X_train, y_train)
print("逻辑回归最佳参数：", grid_search_lr.best_params_)

# 输出逻辑回归最佳模型的得分
best_score_lr = grid_search_lr.best_score_
print("逻辑回归最佳模型的交叉验证得分：", best_score_lr)
