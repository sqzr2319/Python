#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/26 14:46
# @Author: ms169
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams["font.family"] = "FangSong"  # 设置字体为仿宋
matplotlib.rcParams["font.size"] = 14  # 设置字体大小为14


def plot_3dsurf(X, Y, Z):
    # 生成画板，三维坐标系
    fig = plt.figure(figsize=(12, 8))
    ax = plt.axes(projection='3d')

    # 绘制曲面图，添加颜色条
    surf = ax.plot_surface(X, Y, Z, cmap="rainbow", alpha=0.8)
    cbar = fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

    # 定义视角，仰角30度，方位角45度
    ax.view_init(elev=30, azim=45)

    # 添加标签、标题
    ax.set_xlabel("X轴")
    ax.set_ylabel("Y轴")
    ax.set_zlabel("Z轴")
    ax.set_title("3D曲面图")

    # 保存、显示图像
    plt.savefig("8-6.jpg")
    plt.show()


if __name__ == "__main__":
    # 生成x轴、y轴数据、网格坐标矩阵
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)

    # 计算z轴数据
    Z = np.sin(np.sqrt(X ** 2 + Y ** 2)) * np.exp(-0.1 * (X ** 2 + Y ** 2))

    plot_3dsurf(X, Y, Z)
