#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/7/3 23:54
# @Author: ms169
import tensorflow as tf
from tensorflow.keras import layers, models


# CNN模型类
class CNNModel:
    def __init__(self, input_shape=(231, 310), num_classes=4):
        self.model = self.build_model(input_shape, num_classes)

    def build_model(self, input_shape, num_classes):
        model = models.Sequential()
        model.add(layers.Reshape((231, 310, 1), input_shape=(231, 310)))
        model.add(layers.Conv2D(1, (3, 3), activation='relu', input_shape=(231, 310, 1)))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(1, (3, 3), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(1, (3, 3), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Flatten())
        model.add(layers.Dense(512, activation='relu'))
        model.add(layers.Dense(num_classes, activation='softmax'))

        model.compile(optimizer='adam',
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])
        return model
