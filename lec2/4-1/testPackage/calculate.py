#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/24 15:41
# @Author: ms169


def Ccircle(radius):  # 计算圆的周长
    return 2 * 3.14 * radius


def Scircle(radius):  # 计算圆的面积
    return 3.14 * radius ** 2


def Crectangle(length, width):  # 计算矩形的周长
    return 2 * (length + width)


def Srectangle(length, width):  # 计算矩形的面积
    return length * width


def Ctriangle(a, b, c):  # 计算三角形的周长
    return a + b + c


def Striangle(a, b, c):  # 计算三角形的面积
    s = (a + b + c) / 2  # 半周长
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5  # 海伦公式


def Csquare(side):  # 计算正方形的周长
    return 4 * side


def Ssquare(side):  # 计算正方形的面积
    return side ** 2


def main():
    print("圆的周长:", Ccircle(5))
    print("圆的面积:", Scircle(5))
    print("矩形的周长:", Crectangle(4, 6))
    print("矩形的面积:", Srectangle(4, 6))
    print("三角形的周长:", Ctriangle(3, 4, 5))
    print("三角形的面积:", Striangle(3, 4, 5))
    print("正方形的周长:", Csquare(4))
    print("正方形的面积:", Ssquare(4))


if __name__ == "__main__":
    main()
