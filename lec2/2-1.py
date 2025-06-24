#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/24 10:02
# @Author: ms169


def inquiry():  # 查询余额
    print(f"当前余额为：{money}元")


def recharge(change):  # 圈存
    global money
    money += change


def consume(change):  # 刷卡消费
    global money
    money -= change


money = 10000
name = input("请输入师生姓名：")
while 1:
    operator = input("请选择操作：查询余额(i)/圈存(r)/刷卡消费(c)/退出(q)：")
    match operator:
        case "q":
            print("退出成功")
            break
        case "i":
            inquiry()
        case "r":
            while 1:
                change = input("请输入圈存金额：（默认100元）")
                # 获取非负整数
                if change == "":
                    change = 100
                    break
                elif not change.isdigit():
                    print("输入错误")
                else:
                    change = int(change)
                    if change <= 0:
                        print("输入错误")
                    else:
                        break
            recharge(change)
        case "c":
            while 1:
                change = input("请输入消费金额：（默认10元）")
                # 获取非负整数
                if change == "":
                    change = 10
                elif not change.isdigit():
                    print("输入错误")
                    continue
                else:
                    change = int(change)
                    if change <= 0:
                        print("输入错误")
                        continue
                # 判断余额是否足够
                if change > money:
                    print("余额不足")
                else:
                    break
            consume(change)
        case _:
            print("输入错误")
