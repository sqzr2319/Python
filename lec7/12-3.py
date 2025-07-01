#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/7/1 10:04
# @Author: ms169
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv("../data_20250625/housing-0625.csv")
print(data.info())
print(data.describe())

# 用均值填充缺失值
data.fillna(data.mean(), inplace=True)

# 在同一张图上绘制所有特征变量的直方图
plt.figure(figsize=(15, 10))
for i, column in enumerate(data.drop("MEDV", axis=1).columns):
    plt.subplot(4, 4, i + 1)  # 3行4列的子图
    plt.hist(data[column], bins=30, color='blue', alpha=0.7)
    plt.title(column)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('feature_histograms.png')
plt.show()

# 在同一张图上绘制所有特征变量与目标变量之间的散点图
plt.figure(figsize=(15, 10))
for i, column in enumerate(data.drop("MEDV", axis=1).columns):
    plt.subplot(4, 4, i + 1)  # 3行4列的子图
    plt.scatter(data[column], data["MEDV"], alpha=0.5)
    plt.title(f'{column} vs MEDV')
    plt.xlabel(column)
    plt.ylabel('MEDV')
plt.tight_layout()
plt.savefig('feature_vs_target_scatter.png')
plt.show()

# 计算相关系数矩阵
correlation_matrix = data.corr()
# 绘制相关系数矩阵的热力图
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
plt.title('Correlation Matrix')
plt.tight_layout()
plt.savefig('correlation_matrix.png')
plt.show()

# 将数据集划分为特征和目标变量
X_data = data.drop("MEDV", axis=1)
Y_data = data["MEDV"]

# 对CHAS列进行独热编码处理
encoder = OneHotEncoder(sparse_output=False)
X_data_encoded = encoder.fit_transform(X_data[['CHAS']])
# 将编码后的特征与原数据集的其他特征合并
X_data = pd.concat(
    [X_data.drop('CHAS', axis=1), pd.DataFrame(X_data_encoded, columns=encoder.get_feature_names_out(['CHAS']))],
    axis=1)

# 将数据集划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_data, Y_data, test_size=0.3, random_state=42)

# 建立多元线性回归模型，使用基函数
model = LinearRegression()
model.fit(X_train, y_train)

# 输出模型评分、评价指标(MAE,MSE,R^2)
y_pred = model.predict(X_test)
print(f"模型评分(R^2): {r2_score(y_test, y_pred)}")
print(f"均方误差(MSE): {mean_squared_error(y_test, y_pred)}")
print(f"平均绝对误差(MAE): {np.mean(np.abs(y_test - y_pred))}")

# 输出在训练集和测试集上的预测结果，并可视化
train_pred = model.predict(X_train)
test_pred = model.predict(X_test)
plt.figure(figsize=(12, 6))
plt.scatter(y_train, train_pred, alpha=0.5, label='Train Predictions')
plt.scatter(y_test, test_pred, alpha=0.5, label='Test Predictions', color='orange')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2, label='Perfect Prediction')
plt.xlabel('True Values')
plt.ylabel('Predictions')
plt.title('True vs Predicted Values')
plt.legend()
plt.tight_layout()
plt.savefig('predictions_comparison.png')
plt.show()
