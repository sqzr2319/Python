#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/25 10:51
# @Author: ms169


def del_even(num_list):
    del_list = []
    numbers = num_list.copy()  # 复制原列表以保留原始数据
    for num in numbers:
        if num % 2 == 0:
            del_list.append(num)
            num_list.remove(num)
    print("被删除的偶数：", del_list)
    print("剩余的数：", num_list)


if __name__ == "__main__":
    numbers = [1, 2, 4, 5, 6, 8, 10]
    del_even(numbers)
