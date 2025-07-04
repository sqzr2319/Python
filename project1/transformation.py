#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/7/3 23:54
# @Author: ms169
import numpy as np
import pywt
import matplotlib.pyplot as plt


def cwt_to_image(nd_data, image_name, sample_rate=5120, wave_name='morl'):
    """小波变换，生成时频图
    :param: nd_data, 数据片段，一维ndarray
    :param:image_name, 保存的图片名称
    :param:sample_rate, 采样频率，默认5120 HZ
    :param:wave_name, 小波名称
    """

    samples = len(nd_data)  # 采样点数

    # 根据采样频率生成时间轴t
    t = np.linspace(0, samples / sample_rate, samples, endpoint=False)

    # 设置小波函数
    total_scal = 128  # 尺度长度
    fc = pywt.central_frequency(wave_name)  # 小波中心频率
    c_param = 2 * fc * total_scal
    scales = c_param / np.arange(total_scal, 0, -1)

    # 进行连续小波变换
    coefficients, frequencies = pywt.cwt(nd_data, scales, wave_name, 1 / sample_rate)
    amp = abs(coefficients)  # 小波系数矩阵绝对值

    # 生成图像并保存
    plt.figure(figsize=(4, 3))
    plt.contourf(t, frequencies, amp, cmap='jet')
    plt.axis('off')
    plt.savefig(image_name, bbox_inches='tight', pad_inches=0)

    plt.close()
