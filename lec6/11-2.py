#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/30 10:39
# @Author: ms169
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import matplotlib
from scipy.fft import rfft, rfftfreq

matplotlib.rcParams["font.sans-serif"] = "FangSong"  # 设置中文字体
matplotlib.rcParams["font.size"] = 14  # 设置字体大小
matplotlib.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题

data = np.loadtxt("../data_20250625/gear_miss.csv", delimiter=",")
time = np.arange(0, len(data)) / 1024  # 采样频率为1024Hz

plt.figure(figsize=(10, 6))
plt.plot(time, data, label="Original Signal", color='blue')
plt.title("原始信号")
plt.xlabel("时间 (s)")
plt.show()

# 低通滤波器
b, a = signal.butter(5, 100, "low", fs=1000)
filtered_data = signal.filtfilt(b, a, data)

# 快速傅里叶变换
yf = rfft(filtered_data)
xf = rfftfreq(len(data), 1 / 1024)
plt.plot(xf, np.real(yf))  # 取实部绘制频谱
plt.title("信号的频谱")
plt.xlabel("频率 (Hz)")
plt.ylabel("振幅")
plt.xlim(0, 150)  # 限制x轴范围
plt.show()
