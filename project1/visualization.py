#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/7/3 23:55
# @Author: ms169
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib

matplotlib.rcParams["font.family"] = "FangSong"  # 设置字体为仿宋
matplotlib.rcParams["font.size"] = 14  # 设置字体大小为14


def plot_training_history(history):
    """
    可视化训练过程中的损失和准确率变化
    :param history: 模型训练历史
    """
    plt.figure(figsize=(12, 6))

    # 绘制损失曲线
    plt.subplot(1, 2, 1)
    plt.plot(history['loss'], label='训练损失')
    plt.plot(history['val_loss'], label='验证损失')
    plt.title('训练和验证损失')
    plt.xlabel('轮次')
    plt.ylabel('损失')
    plt.legend()

    # 绘制准确率曲线
    plt.subplot(1, 2, 2)
    plt.plot(history['accuracy'], label='训练准确率')
    plt.plot(history['val_accuracy'], label='验证准确率')
    plt.title('训练和验证准确率')
    plt.xlabel('轮次')
    plt.ylabel('准确率')
    plt.legend()

    plt.tight_layout()
    plt.show()
