#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/7/2 08:45
# @Author: ms169
import numpy as np
import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers, models
from matplotlib import pyplot as plt

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# 显示前32张训练图片（4行8列）
plt.figure(figsize=(12, 6))
for i in range(32):
    plt.subplot(4, 8, i + 1)
    plt.imshow(x_train[i], cmap='gray')
    plt.title(f'Label: {y_train[i]}')
    plt.axis('off')
plt.tight_layout()
plt.show()

# 建立CNN模型
model = models.Sequential()
model.add(layers.Reshape((28, 28, 1), input_shape=(28, 28)))
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

# 编译模型
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 输出模型结构
model.summary()

# 训练模型
history = model.fit(x_train, y_train, epochs=5, batch_size=64, validation_split=0.2)

# 训练过程可视化
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# 将模型保存到文件
model.save('13-2.keras')

# 加载模型
loaded_model = keras.models.load_model('13-2.keras')

# 在测试集上预测
test_loss, test_acc = loaded_model.evaluate(x_test, y_test, verbose=2)
print('\nTest accuracy:', test_acc)

# 显示前32张预测错误的图片（4行8列）
predictions = loaded_model.predict(x_test)
incorrect_indices = np.where(np.argmax(predictions, axis=1) != y_test)[0][:32]
plt.figure(figsize=(12, 6))
for i, idx in enumerate(incorrect_indices):
    plt.subplot(4, 8, i + 1)
    plt.imshow(x_test[idx], cmap='gray')
    plt.title(f'Predicted: {np.argmax(predictions[idx])}\nActual: {y_test[idx]}')
    plt.axis('off')
plt.tight_layout()
plt.show()
