#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/23 15:59
# @Author: ms169


# 接收键盘输入的月份和年龄
while 1:
    month = int(input("请输入月份："))
    if month < 1 or month > 12:
        print("月份输入错误！")  # 当输入月份为 1-12 以外的值，给出错误输入提示
    else:
        break

while 1:
    age = int(input("请输入年龄："))
    if age < 0 or age > 100:
        print("年龄输入错误！")  # 当输入年龄为 0-100 以外的值，给出错误输入提示
    else:
        break

# 计算颐和园门票价格并输出至屏幕
if 4 <= month <= 10:
    price = 30
else:
    price = 20

if age < 6:
    price = 0
elif age < 18:
    price /= 2
elif age > 60:
    price = 0

print("票价：", price)
