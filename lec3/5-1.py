#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/6/25 09:04
# @Author: ms169
import shutil

#  创建一个CSV文件并写入学生信息
f = open("../data_20250625/2024013328.csv", "w", encoding="utf-8")
f.write("学号,姓名,性别,成绩\n")
for i in range(5):
    print(f"请输入第{i + 1}个学生的信息：")
    identity = input("学号：")
    name = input("姓名：")
    gender = input("性别：")
    score = int(input("成绩："))
    f.write(f"{identity},{name},{gender},{score}\n")
f.close()
shutil.copy("../data_20250625/2024013328.csv", "2024013328.csv.backup")

# 读取备份文件并打印内容
with open("2024013328.csv.backup", "r", encoding="utf-8") as f:
    contents = f.readlines()
    for line in contents:
        print(line.strip())
