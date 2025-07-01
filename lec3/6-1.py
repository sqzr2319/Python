#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/25 10:19
# @Author: ms169


def quadratic(a, b, c):
    try:
        d = b ** 2 - 4 * a * c
        assert d >= 0, "判别式小于0，方程无实数解"
    except AssertionError as e:  # 捕获判别式小于0的异常
        print(e)
        exit(1)
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return x1, x2


if __name__ == "__main__":
    try:
        a = input("请输入a的值：")
        assert a.isdigit() and int(a) != 0, "a必须是非零整数"
        a = int(a)
    except AssertionError as e:  # 捕获a为0或非整数的异常
        print(e)
        exit(1)

    try:
        b = input("请输入b的值：")
        assert b.isdigit(), "b必须是整数"
        b = int(b)
    except AssertionError as e:  # 捕获b为非整数的异常
        print(e)
        exit(1)

    try:
        c = input("请输入c的值：")
        assert c.isdigit(), "c必须是整数"
        c = int(c)
    except AssertionError as e:  # 捕获c为非整数的异常
        print(e)
        exit(1)

    r1, r2 = quadratic(a, b, c)
    print(f"x1={r1}, x2={r2}")
