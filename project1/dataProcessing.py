#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/7/4 01:04
# @Author: ms169
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from matplotlib import pyplot as plt
from concurrent.futures import ThreadPoolExecutor


# 数据处理类
class DataProcessing:
    def __init__(self):
        self.images = np.array([]).reshape(0, 231, 310)
        self.labels = np.array([])

    from concurrent.futures import ThreadPoolExecutor

    def load_images(self):  # 处理图片
        # 预分配内存
        self.images = np.zeros((4000, 231, 310), dtype=np.float32)
        processed_count = 0

        # 定义处理单张图片的函数
        def process_image(idx):
            nonlocal processed_count
            image_name = f"images/image_{idx}.png"
            image = plt.imread(image_name)
            # 将伪彩色图转成灰度图
            gray_img = image[:, :, 0] * 0.2989 + image[:, :, 1] * 0.5870 + image[:, :, 2] * 0.1140
            # 标准化
            norm_img = (gray_img - np.mean(gray_img)) / np.std(gray_img)
            processed_count += 1
            return idx, norm_img

        # 使用8个线程并行处理
        with ThreadPoolExecutor(max_workers=8) as executor:
            for idx, result in executor.map(lambda i: process_image(i), range(4000)):
                self.images[idx] = result

    def load_labels(self):  # 处理标签
        # 直接创建标签数组
        self.labels = np.repeat(np.arange(4), 1000)

        # 独热编码
        encoder = OneHotEncoder(sparse_output=False)
        self.labels = encoder.fit_transform(self.labels.reshape(-1, 1))

    def process_data(self):  # 划分数据集
        self.load_images()
        self.load_labels()
        train_images, test_images, train_labels, test_labels = train_test_split(self.images, self.labels, test_size=0.2,
                                                                                random_state=42)
        return train_images, test_images, train_labels, test_labels
