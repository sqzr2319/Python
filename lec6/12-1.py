#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/30 14:50
# @Author: ms169
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

data = pd.read_csv("../data_20250625/cs-training-0625.csv")

# 去除异常值
columns = ["Age"]
for col in columns:
    q1 = data[col].quantile(0.25)
    q3 = data[col].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    data = data[(data[col] >= lower_bound) & (data[col] <= upper_bound)]

# 用中位数填充缺失值（负债率、月收入为对数正态分布，使用中位数更稳健）
for col in data.select_dtypes(include=[np.number]).columns:
    median_value = data[col].median()
    data[col] = data[col].fillna(median_value)

# 数据集中Serious列为1的数据过少，进行数据增广
serious_samples = data[data["Serious"] == 1].sample(n=1000, replace=True, random_state=42)
non_serious_samples = data[data["Serious"] == 0]
data = pd.concat([serious_samples, non_serious_samples], ignore_index=True)

data.to_csv("../data_20250625/appended.csv", index=False)

# 将数据集划分为特征和目标变量
X_data = data.drop("Serious", axis=1)
Y_data = data["Serious"]

# 创建缩放器，数据标准化处理
trans = StandardScaler()
trans.fit(X_data)
normalized_X = trans.transform(X_data)

# 创建独热编码器, 对目标变量进行编码（输入须为矩阵）
encoder = OneHotEncoder(sparse_output=False)
Y_matrix = Y_data.to_numpy().reshape(-1, 1)
encoder.fit(Y_matrix)
encode_Y = encoder.transform(Y_matrix)

# 将数据划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(normalized_X, encode_Y, test_size=0.3, random_state=42)
print("训练集和测试集划分完成。")

# 建立scikit-learn估计器（分类模型）
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# 将独热编码转换为类索引
y_test_classes = np.argmax(y_test, axis=1)
y_pred_classes = np.argmax(y_pred, axis=1)

# 模型评价
print(f"模型评分(acc):{accuracy_score(y_test_classes, y_pred_classes)}")
print("准确率：", accuracy_score(y_test_classes, y_pred_classes))
print("精确率：", precision_score(y_test_classes, y_pred_classes, average='weighted', zero_division=0))
print("召回率：", recall_score(y_test_classes, y_pred_classes, average='weighted', zero_division=0))

# 输出在训练集和测试集上的预测结果
train_pred = model.predict(X_train)
test_pred = model.predict(X_test)
train_categories = encoder.inverse_transform(train_pred)
test_categories = encoder.inverse_transform(test_pred)
print("训练集预测结果：", train_categories[:5])  # 只显示前5个预测结果
print("测试集预测结果：", test_categories[:5])
