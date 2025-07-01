#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/7/1 15:25
# @Author: ms169
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras import layers, models

data = pd.read_csv("../data_20250625/housing-0625.csv")

# 用均值填充缺失值
data.fillna(data.mean(), inplace=True)

# 将数据集划分为特征和目标变量
X_data = data.drop("MEDV", axis=1)
Y_data = data["MEDV"]

# 对除CHAS外的列标准化
columns = X_data.columns.drop("CHAS")
scaler_X = StandardScaler()
X_data[columns] = scaler_X.fit_transform(X_data[columns])
scaler_Y = StandardScaler()
Y_data = scaler_Y.fit_transform(Y_data.values.reshape(-1, 1))

# 将数据集划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_data, Y_data, test_size=0.3, random_state=42)

# 构建神经网络模型
model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(1))

# 输出模型结构
model.summary()

# 编译和训练模型
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])
history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2, verbose=1)

# 可视化训练过程
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['mae'], label='Training MAE')
plt.plot(history.history['val_mae'], label='Validation MAE')
plt.title('Training and Validation MAE')
plt.xlabel('Epochs')
plt.ylabel('Mean Absolute Error')
plt.legend()
plt.tight_layout()
plt.savefig('training_history.png')
plt.show()

# 模型评价与预测
y_pred = model.predict(X_test)
mse = tf.keras.metrics.MeanSquaredError()
mse.update_state(y_test, y_pred)
r2 = tf.keras.metrics.R2Score()
r2.update_state(y_test, y_pred)
print(f'Mean Squared Error: {mse.result().numpy()}')
print(f'R-squared: {r2.result().numpy()}')

# 对测试集、预测结果反标准化
y_pred = model.predict(X_test)
y_test_array = y_test.reshape(-1, 1)
y_test_rescaled = scaler_Y.inverse_transform(y_test_array)
y_pred_rescaled = scaler_Y.inverse_transform(y_pred)

# 可视化输出
plt.figure(figsize=(10, 6))
plt.scatter(y_test_rescaled, y_pred_rescaled, alpha=0.5)
plt.plot([y_test_rescaled.min(), y_test_rescaled.max()],
         [y_test_rescaled.min(), y_test_rescaled.max()], 'k--', lw=2)
plt.title('True vs Predicted Values')
plt.xlabel('True Values')
plt.ylabel('Predicted Values')
plt.tight_layout()
plt.savefig('true_vs_predicted.png')
plt.show()

# 保存模型
model.save('13-1.keras')
