#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/24 08:42
# @Author: ms169
import random

options_tuple = ("石头", "剪刀", "布")
win_dict = dict([("石头", "剪刀"), ("剪刀", "布"), ("布", "石头")])

while 1:
    player_choice = input("请输入你的选择（石头剪刀布）或输入 quit 退出: ")
    if player_choice == "quit":
        print("游戏结束")
        break
    elif player_choice not in options_tuple:
        print("输入错误")
        continue
    pc_choice = random.choice(options_tuple)
    print(f"电脑选择了{pc_choice}")
    match win_dict[player_choice] == pc_choice:
        case 1:
            print("你赢了")
        case 0 if player_choice == pc_choice:
            print("平局")
        case _:
            print("你输了")
